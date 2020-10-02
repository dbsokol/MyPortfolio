from django.shortcuts import render
from Tools import tools


@tools.monitor_me()
def RenderTasksPage(request):
    
    context = {'status' : 0}
    
    return render(request, 'tasks.html', context=context)