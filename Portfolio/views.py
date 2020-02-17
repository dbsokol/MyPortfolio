from django.http import HttpResponse
from django.shortcuts import render
import json


def LoadPortfolio(request):
    
    context = {'status': 0}
    
    return render(request, 'portfolio.html', context=context)
    
    
    
def Render404(request, exception):
    
    context = {'status' : 404}
    
    return render(request, '404.html', context=context)
    

def TestHTML(request):

    context = {'status': 0}

    return render(request, 'test.html', context=context) 