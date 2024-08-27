from django.urls import path
#Importamos el modulo vistas
from . import views


#Esta cadena se añade para poder diferenciar las urls de nuestras rutas (name) con las de las otras aplicaciones que se llamen igual
app_name = "polls"

urlpatterns = [
    #Ponemos la ruta que se necesita para entrar, nombre de la funcion en el modulo y nombre
    #Ahora solo queda definir la ruta a nivel de proyecto

    path("primera_vista/", views.IndexView.as_view(), name="index"),

    #Se muestra como se definen los datos que ingresa el usuario por medio de la URL, en Views se muestra como hacer para que estos valores se vean en pantalla
    #Especificamos el tipo de dato que el usuario debe ingresar, este llegara al argumento de la funcion que definimos en views.py
    # ex: /polls/
    path("especificos_name/<int:pk>/", views.DetailView.as_view(), name="ejemplo_name"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"), #CAMBIAMOS Resultsview y añadimos .as_view
    # ex: /polls/5/vote/
    path("<int:dato_usuario_nav>/vote/", views.vote, name="vote"),

]

