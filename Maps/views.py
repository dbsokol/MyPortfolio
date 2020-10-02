from ip2geotools.databases.noncommercial import DbIpCity
from django.views.decorators.cache import never_cache
from .CountryCodes import country_codes
from django.shortcuts import render
from .models import Visitor
from Tools import tools
import pandas as pd
import numpy as np
import json



@never_cache
@tools.monitor_me()
def Visitors(request):
    
    # get dataframe of all visitors:
    all_visitors = Visitor.objects.all().values()
    all_visitors = pd.DataFrame(all_visitors)
    
    # convert to json data:
    visitors = all_visitors
    visitors['latitude'] = visitors['latitude'].astype(float)
    visitors['longitude'] = visitors['longitude'].astype(float)
    visitors['visit_date'] = pd.to_datetime(visitors['visit_date'], errors='coerce')
    visitors['visit_date'] = visitors['visit_date'].dt.strftime('%Y-%m-%d')
    
    # get nearest lat/long to 5 degrees:
    visitors['nearest_longitude'] = visitors['longitude'].apply(lambda x: int(5 * round(float(x)/5)))
    visitors['nearest_latitude'] = visitors['latitude'].apply(lambda x: int(5 * round(float(x)/5)))

    # organize by nearest lat/long and city:    
    visitors = visitors.groupby(['nearest_latitude', 'nearest_longitude', 'city']).count()
    visitors = visitors.sort_values('id')
    visitors = visitors.groupby(['nearest_latitude', 'nearest_longitude']).tail(1)['id']
    visitors = visitors.reset_index().rename(columns={'id':'count'})
    
    # append count ratio relative to all visitors:
    visitors['count_ratio'] = visitors['count'] / visitors['count'].sum()
    visitors['sigmoid_ratio'] = 1.0 / (1.0 + np.exp(-3 * (visitors['count_ratio'] - 0.6) ))
    
    # convert to dictionary:
    visitors = visitors.to_dict(orient='records')
    
    # group by country:
    visitors_by_country = all_visitors.groupby('country_full_name').count()['id']
    visitors_by_country = visitors_by_country.reset_index()
    visitors_by_country = visitors_by_country.rename(columns={'country_full_name':'name', 'id':'count'})
    visitors_by_country = visitors_by_country.to_dict(orient='records')
    
    totals = {
        'count' : all_visitors.shape[0],
        'country' : all_visitors.groupby('country_full_name').count().reset_index().max().country_full_name,
    }
    
    # pack context:
    context = {
        'countries' : visitors_by_country,
        'visitors' : visitors,
        'totals' : totals,
        'status' : 0,
    }
    
    return render(request, 'visitors.html', context=context)



@tools.monitor_me()    
def Render404(request, exception):
    
    # get, lookup ip address:
    ip_address = request.META['HTTP_X_REMOTE_ADDR']
    ip_lookup = DbIpCity.get(ip_address, api_key='free')
    
    # convert ip_lookup to python dictionary:
    visitor_kwargs = json.loads(ip_lookup.to_json())
    
    # look up, add add country full name:
    visitor_kwargs['country_full_name'] = country_codes[visitor_kwargs['country']]
    
    # add missng elements to visitor object:
    if visitor_kwargs['latitude'] is None:
        
        # check city name:
        if visitor_kwargs['city'] == 'Moscow (Tsentralnyy administrativnyy okrug)':
            visitor_kwargs['latitude'] = 37.613
            visitor_kwargs['longitude'] = 55.767
            
        if visitor_kwargs['city'] == 'Zarvanytsya':
            visitor_kwargs['latitude'] = 49.219
            visitor_kwargs['longitude'] = 25.371
    
    # create visitor object:
    visitor = Visitor.objects.create(**visitor_kwargs)
    visitor.save()
    
    # pack context:
    context = {'status' : 404}
    
    return render(request, '404.html', context=context)