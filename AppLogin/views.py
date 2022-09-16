from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

from .models import Login


def home(request):
    return HttpResponse("SignIn")

def login(request):
    homehtml=open("C:/Users/Nestor/Documents/Coder - Desarrollo Web/Python/Proyecto entrega/TrabajoEnCasa/WorkHome/template/home.html")
    plantilla=Template(homehtml.read())
    homehtml.close()
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
  