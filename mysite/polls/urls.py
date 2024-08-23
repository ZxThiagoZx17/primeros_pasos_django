from django.urls import path
#Importamos el modulo vistas
from . import views

urlpatterns = [
    #Ponemos la ruta que se necesita para entrar, nombre de la funcion en el modulo y nombre
    #Ahora solo queda definir la ruta a nivel de proyecto

    path("primera_vista/", views.index, name="index"),

    #Se muestra como se definen los datos que ingresa el usuario por medio de la URL, en Views se muestra como hacer para que estos valores se vean en pantalla
    #Especificamos el tipo de dato que el usuario debe ingresar, este llegara al argumento de la funcion que definimos en views.py
    # ex: /polls/
    path("<int:dato_usuario_nav>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:dato_usuario_nav>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:dato_usuario_nav>/vote/", views.vote, name="vote"),

]