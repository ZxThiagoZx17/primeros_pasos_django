from django.urls import path
#Importamos el modulo vistas
from . import views

urlpatterns = [
    #Ponemos la ruta que se necesita para entrar, nombre de la funcion en el modulo y nombre
    #Ahora solo queda definir la ruta a nivel de proyecto

    path("primera_vista/", views.index, name="index"),

    #Se muestra como se definen los datos que ingresa el usuario por medio de la URL, en Views se muestra como hacer para que estos valores se vean en pantalla
    # ex: /polls/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

]