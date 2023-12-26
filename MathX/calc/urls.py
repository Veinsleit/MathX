from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('algcalc/', views.algcalc, name='algcalc'),
    path('algcalc/alganswer/', views.alganswer, name='alganswer'),
    path('algcalc/algex/', views.algex, name='algex'),
    path('algcalc/algex/alganswer', views.alganswer, name='alganswer'),
    path('algtotrig/', views.algtotrig, name='algtotrig'),
    path('algtotrig/convz', views.convz, name='convz'),
    path('algtotrig/convzex', views.convzex, name='convzex'),
    path('algtotrig/convzex/convz', views.convz, name='convz'),
    path('trigcalc/', views.trigcalc, name='trigcalc'),
    path('trigcalc/triganswer', views.triganswer, name='triganwser'),  
    path('trigcalc/trigex', views.trigex, name='trigex'),  
    path('trigcalc/trigex/triganswer', views.triganswer, name='triganwser'),  
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]

