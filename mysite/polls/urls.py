from django.urls import path
#Importamos el modulo vistas
from . import views

urlpatterns = [
    #Ponemos la ruta que se necesita para entrar, nombre de la fucion en el modulo y nombre
    #Ahora solo queda definir la ruta a nivel de proyecto
    path("primera_vista/", views.index, name="index"),
]