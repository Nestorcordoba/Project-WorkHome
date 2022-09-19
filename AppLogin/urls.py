from django.urls import path

from .views import *

urlpatterns =[
    path('login/',login_request, name='login'),
    path('home/',home, name='home'),
    path('', home)
]