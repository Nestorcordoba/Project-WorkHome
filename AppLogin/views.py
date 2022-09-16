from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

from .models import Login


def login(request):
    homehtml1=open("C:/Users/Nestor/Documents/Coder - Desarrollo Web/Python/Proyecto entrega/TrabajoEnCasa/WorkHome/template/login.html")
    plantilla1=Template(homehtml1.read())
    homehtml1.close()
    contexto1=Context()
    documento1=plantilla1.render(contexto1)
    return HttpResponse(documento1)

def home(request):
    homehtml=open("C:/Users/Nestor/Documents/Coder - Desarrollo Web/Python/Proyecto entrega/TrabajoEnCasa/WorkHome/template/home.html")
    plantilla=Template(homehtml.read())
    homehtml.close()
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
  