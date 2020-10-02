from django.urls import path
from . import views

urlpatterns = [
    path('visitors/', views.Visitors, name='visitors'),
]
