from django.urls import path

from .views import *

urlpatterns =[
    path('login/',viewLoin, name='login'),
    path('home/',home, name='home'),
    path('', home)
]