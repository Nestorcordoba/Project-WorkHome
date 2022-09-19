
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

#imports para login
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .forms import UserRegisterForm

def home(request):
   return render(request, "AppLogin/home.html")


def login_request(request):
   if request.method=="POST":
      form=AuthenticationForm(request, data=request.POST)
      if form.is_valid():
         #info=miFormulario.cleaned_data
         usu=request.POST["username"]
         clave=request.POST["password"]
         usuario=authenticate(username=usu,password=clave)
         if usuario is not None:
            login(request,usuario)
            return render(request, 'AppLogin/login.html', {'mensaje':f"Bienvenido {usuario}"})
         else:
            return render(request, 'AppLogin/login.html', {"formulario":form, 'mensaje': 'Usuario o contraseña incorrectos'})
      else:
         return render(request, "AppLogin/login.html", {"formulario":form, 'mensaje': 'Formulario invalido'})
   else:
      form=AuthenticationForm()
      return render(request, "AppLogin/login.html", {"formulario":form})

def register_request(request):
   if request.method=="POST":
      form=UserRegisterForm(request.POST)
      if form.is_valid():
         username=form.cleaned_data["username"]
         form.save()
         return render(request, 'AppLogin/registro.html', {'mensaje':f"Usuario {username} creado"})
   else:
      form=UserRegisterForm()
   return render(request, 'AppLogin/registro.html', {"formulario":form})
   

