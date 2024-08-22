"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#Include nos permite hacer referencia a otros archivos urls.py
#Siempre debes usar include() cuando incluye otros patrones de URL. admin.site.urls es la única excepción a esto.

#En path se usan 4 argumentos route y view que son obligatorios y  kwargs, y name

#Route: String que contiene el patron de URL, tomara primero este y luego el de URLS.py a nivel de APP.
#View: Es una funcion de vista include() o as_view() para vistas basadas en clases
#Kwargs: Permite pasar argumentos adicionales a la vista función o método
#Name: Se usa para nombrar patrones de URL, permite referirse a ella en otra parte del archivo sin usar ambiguedades dando respuestas claras
from django.urls import path, include

urlpatterns = [
    path('polls/', include("polls.urls")),
    path('admin/', admin.site.urls),
]
#Para ingresa se usa http://127.0.0.1:8000/polls/primera_vista/ en este caso