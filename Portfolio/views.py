from django.shortcuts import render

# Create your views here.
def LoadPortfolio(request):
    
    context = {
        'test' : 'this is a test',
    }
    
    return render(request, 'portfolio.html', context=context)