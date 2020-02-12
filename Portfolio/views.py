from django.http import HttpResponse
from django.shortcuts import render
import json


def LoadPortfolio(request):
    
    context = {'status': 0}
    
    return render(request, 'portfolio.html', context=context)
    
    

def TestHTML(request):

    context = {'status': 0}

    return render(request, 'test.html', context=context) 