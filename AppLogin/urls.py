from django.urls import path

from .views import *

urlpatterns =[
    path('home/',home, name='home'),
    path('login/',login_request, name='login'),
    path('registro/',register_request, name='registro'),
    path('', home)
]