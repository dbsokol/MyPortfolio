from django.db.models.signals import post_save, pre_delete
from datetime import datetime
from .models import Visitor
from Tools import tools
import pandas as pd
import numpy as np
import folium
import os



def GetAllVisitors():
    
    ''' Queries database for visitors, returns data as dataframe '''
    
    # get all visitors in database, convert to dataframe:
    all_visitors = Visitor.objects.all().values()
    all_visitors = pd.DataFrame(all_visitors)
    
    return all_visitors



def ParseVisitors(visitors):
    
    ''' Accepts visitors dataframe, appends nearest lat/long values '''
    
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
    visitors['sigmoid_ratio'] = 1.0 / (1.0 + np.exp(-5 * (visitors['count_ratio'] - 0.5) ))
    
    return visitors



def CreateMap(visitors):
    
    ''' Accepts visitor, dataframe of all visitors, creates visitor_map.html file '''
    
    # initialize variables:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    map_file = os.path.join(BASE_DIR, 'Templates/map.html')
    
    # initilaize map:
    map = folium.Map(
        location=[0, 0],
        tiles='Stamen Watercolor',
        zoom_start=3,
    )
    
    # define circle marker creator:
    def CreateCircleMarker(row):
    
        if row['count'] > 1:
            popup = str(row['count']) + ' hits near ' + str(row['city'])
        else:
            popup = str(row['count']) + ' hit near ' + str(row['city'])
    
        # create circles:
        circle_marker = folium.CircleMarker(
            location = [row['nearest_latitude'], row['nearest_longitude']],
            radius = 50*row['sigmoid_ratio'],
            popup = popup,
            color = '#3186cc',
            fill = True,
            fill_color = '#3186cc'
        )
        
        # add to map:
        circle_marker.add_to(map)
        
    # add circle marker to map:
    visitors.apply(lambda x: CreateCircleMarker(x), axis=1)
    
    map.save(map_file)



def BuildMap(sender, **kwargs):
    
    # exits function on object creation (so that function is only run once on save):
    if 'created' in kwargs:
        if kwargs['created']:
            return 
    
    # Step 1) get all visitors:
    all_visitors = GetAllVisitors()

    # Step 2) parse visitors:
    visitors = ParseVisitors(all_visitors)

    # Step 3) create map:
    CreateMap(visitors)
    
    print('[%s] [Maps.MapBuilder.BuildMap] Updated map.' %(datetime.now().strftime('%d/%b/%Y %H:%M:%S')))


