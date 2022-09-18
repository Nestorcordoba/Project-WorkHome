
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template


from .models import ModelLogin
from AppLogin.forms import Formslogin


def home(request):
  return render(request, "AppLogin/home.html")



def viewLoin(request):
   if request.method=="POST":
      miFormulario=Formslogin(request.POST)
      if miFormulario.is_valid():
         info=miFormulario.cleaned_data
         useremail=info.get("useremail")
         password=info.get("password")
         login=ModelLogin(useremail=useremail,password=password)
         login.save()
         return render(request, "AppLogin/login.html", {"mensaje": "Has iniciado Sesion"})
      else:
         return render(request, "AppLogin/login.html", {"mensaje": "Error"})
   else:
      miFormulario=Formslogin()
      return render(request, "AppLogin/login.html", {"formulario":miFormulario})


