from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trig/', views.trig, name='trig'),
    path('zconv/', views.conv, name='zconv'),
    path('result/', views.calc, name='result'),
    path('zconv/resultz/', views.convz, name='resultz'),
]

