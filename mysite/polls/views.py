from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.

#Creamos una vista simple en django, ahora tenemos que definirle una url
# def index(request):
#     return HttpResponse("Hola bebe este es el index request")

#Definimos las vistas para mostrar como podemos anexar datos que ingrese el usuario en la url en la pagina principal
def detail(request, dato_usuario_nav):
    return HttpResponse("Estas mirando la pregunta numero: %s." % dato_usuario_nav)
#Es importante usar los formatos "%s" y "%" para que funcione bien

def results(request, dato_usuario_nav):
    response = "Y Estas mirando los resultados de la pregunta %s."
    return HttpResponse(response % dato_usuario_nav)


def vote(request, dato_usuario_nav):
    return HttpResponse("Tu voto en la pregunta es de: %s." % dato_usuario_nav)

#Una vista puede hacer 2 cosas, o devolver un HttpResponse con el contenido HTML que queremos ver o hacer un excepcion con Http404

#Comentamos la vista index y creamos una nueva, esta lo que hace es mostrarnos todos los objetos del modelo Questions odenado por fecha de publicacion separados por , 

# def index(request):
#     ultimas_preguntas_hechas = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in ultimas_preguntas_hechas])
#     return HttpResponse(output)

#Funciona correctamente pero no es lo correcto codificar el diseño de pagina desde codigo de py, lo mejor es usar el sistema de plantillas 

#Creamos un directorio "templates" Django siempre buscara las plantillas ahi

#Esta vendria a ser la funcion de vista usada para la plantilla
def index(request):
    ultimas_preguntas_hechas = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "ultimas_preguntas_hechas": ultimas_preguntas_hechas,
    }
    return HttpResponse(template.render(context, request))

#Este codigo carga la platilla polls/index.html, contexto es un diccionario que mapea nombres de variables de plantilla a objetos