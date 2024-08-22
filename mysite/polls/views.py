from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Creamos una vista simple en django, ahora tenemos que definirle una url
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")