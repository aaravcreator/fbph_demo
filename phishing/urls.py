from django.urls import path
from .views import index,ullu
urlpatterns  = [
    path('',index,name='index'),
    path('ullu/',ullu,name='ullu')
]