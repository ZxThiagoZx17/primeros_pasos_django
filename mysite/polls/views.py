from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Creamos una vista simple en django, ahora tenemos que definirle una url
def index(request):
    return HttpResponse("Hola bebe este es el index request")

#Definimos las vistas para mostrar como podemos anexar datos que ingrese el usuario en la url en la pagina principal
def detail(request, dato_usuario_nav):
    return HttpResponse("Estas mirando la pregunta numero: %s." % dato_usuario_nav)
#Es importante usar los formatos "%s" y "%" para que funcione bien

def results(request, dato_usuario_nav):
    response = "Y Estas mirando los resultados de la pregunta %s."
    return HttpResponse(response % dato_usuario_nav)


def vote(request, dato_usuario_nav):
    return HttpResponse("Tu voto en la pregunta es de: %s." % dato_usuario_nav)