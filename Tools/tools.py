from ip2geotools.databases.noncommercial import DbIpCity
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from time import time
import traceback
import pickle
import json
import ast




def PrintTitle(function_name):
    
    border = '   [' + '#' * (len(function_name) + 10) + ']\n'
    middle = '   [##| [' + function_name + '] |##]\n'  
    
    print('\n' + border + middle + border)
    


# Decorator tools:
def monitor_me(verbose_level=2, save_output=False):
    
    ''' monitor_me decorator, used to time execution time of functions and handle errors '''
    
    def decorator(function):
        
        def wrapper(*args, **kwargs):
        
            # intialize result object:
            result = {}
        
            # set fuction full name:
            module_name = function.__code__.co_filename.split('/')[-2] + '.' + function.__code__.co_filename.split('/')[-1]
            module_name = module_name.replace('.py','') 
            function_full_name = module_name + '.' + function.__name__
            
            # start timer:
            function_start = time()
            
            # exception handler:
            # try to execute function:
            try:
                content = function(*args, **kwargs)
                status = 0
                status_message = 'Success'
                
            # capture traceback on failure:
            except:
                content = None
                status = 1
                status_message = 'Failure [%s]' %(traceback.format_exc())
            
            # terminate timer:
            function_end = time()

            # try to get status from context object in http response object:
            # applicable if view function returns a unique status code:
            try:
                status = ast.literal_eval(content.content.decode('utf-8'))['status']
            except:
                pass
                
            # try to access request object:
            try:
                request = args[0]
                post = request.POST
                method = request.method
                ip_address = request.META['HTTP_X_REMOTE_ADDR']
                
            except:
                request = None
                post = 'unknown'
                method = 'unknown'
                ip_address = 'unknown'
                
            # try to geolocate ip address:
            try:
                response = DbIpCity.get(ip_address, api_key='free')
                country = response.country
                state = response.region
                city = response.city
                
            except:
                response = None
                country = 'unknown'
                state = 'unknown'
                city = 'unknown'
            
            # get current time:
            current_time = datetime.now().strftime('%d/%b/%Y %H:%M:%S')

            # build message:
            message = "[%s] [%s] [Status: %s] [Message: %s] Function execution time [%7.2f s]" %(current_time, function_full_name, status, status_message, function_end-function_start)

            # print title:
            if verbose_level>=3:
                PrintTitle(function_full_name)

            # print request:
            if verbose_level>=2:
                print('[%s] [%s] Received [%s] request from [%s] with [%s]' %(current_time, function_full_name, method, ip_address, post))
                print('[%s] [%s] Geolocation best guess [%s, %s, %s]' %(current_time, function_full_name, country, state, city))
        
            # print execution time when verbose is true:
            if verbose_level>=1:
                print(message)
        
            # exception handler:
            if content is None:
                content = HttpResponse(json.dumps({'message': message, 'status' : status}), content_type='application/json')
        
            # pack result object:
            result['content'] = content
            result['status'] = status
            result['message'] = 'There was an error when processing your request, please contact support@airplant.garden for assistance.'
        
            # save output to .pkl file if save_output = True:
            if save_output:
                with open('/tmp/' + function.__name__ + '.pkl', 'wb') as handle:
                    pickle.dump(result, handle)
            
            return result['content']
        
        return wrapper
    
    return decorator
    
    
    
class dotdict(dict):
    
    '''dot.notation access to dictionary attributes'''
    
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__