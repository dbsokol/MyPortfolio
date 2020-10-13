from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoadPortfolio, name='home'),
    path('test/', views.TestHTML, name='test'),
    path('icardio-ai/', views.RenderICardioAi, name='icardio-ai'),
    path('portfolio2', views.RenderPortfolio2, name='portfoilio2')
]
