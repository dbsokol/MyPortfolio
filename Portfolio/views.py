from django.shortcuts import render
from Tools import tools



@tools.monitor_me()
def LoadPortfolio(request):
    
    context = {'status': 0}
    
    return render(request, 'portfolio.html', context=context)
    
    
    
@tools.monitor_me()    
def RenderPortfolio2(request):
    
    context = {'status': 0}
    
    return render(request, 'portfolio/portfolio.html', context=context)
    
    
    
@tools.monitor_me()    
def RenderICardioAi(request):
    
    context = {'status': 0}
    
    return render(request, 'icardio.ai.html', context=context)
    


@tools.monitor_me()
def TestHTML(request):

    context = {'status': 0}

    return render(request, '404.html', context=context) 