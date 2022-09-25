from django.urls import path, include

from AppLogin.views import *
from Blogs.views import *
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('home/',home, name='home'),
    path('login/',login_request, name='login'),
    path('registro/',register_request, name='registro'),
    path('', home),
    path('logout/', LogoutView.as_view(template_name='AppLogin/logout.html'), name='logout'),
    path('edicionPerfil/', edicionPerfil, name='edicionPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('crearPost/', crear_post, name= 'crearPost'),
]