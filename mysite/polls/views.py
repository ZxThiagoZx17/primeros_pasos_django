from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Creamos una vista simple en django, ahora tenemos que definirle una url
def index(request):
    return HttpResponse("Hola bebe este es el index request")

#Definimos las vistas para mostrar como podemos anexar datos que ingrese el usuario en la url en la pagina principal
def detail(request, question_id):
    return HttpResponse("Estas mirando la pregunta numero: %s." % question_id)


def results(request, question_id):
    response = "Y Estas mirando los resultados de la pregunta %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Tu voto en la pregunta es de: %s." % question_id)