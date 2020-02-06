from django.shortcuts import render

# Create your views here.
def LoadPortfolio(request):
    
    print('hello i am in here')
    
    context = {
        'test' : 'this is a test2 test3',
    }
    
    return render(request, 'portfolio.html', context=context)