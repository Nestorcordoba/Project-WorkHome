from pipes import Template
from django.http import HttpResponse
from django.template import Context, Template,loader


def home(request):
    return HttpResponse("SignIn")

def login(request):
    homehtml=open("C:/Users/Nestor/Documents/Coder - Desarrollo Web/Python/Proyecto entrega/TrabajoEnCasa/WorkHome/Plantillas/home.html")
    plantilla=Template(homehtml.read())
    homehtml.close()
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
  

