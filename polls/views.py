from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.template import loader
from django.db.models import F
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

#Creamos una vista simple en django, ahora tenemos que definirle una url
# def index(request):
#     return HttpResponse("Hola bebe este es el index request")

#Definimos las vistas para mostrar como podemos anexar datos que ingrese el usuario en la url en la pagina principal
# def detail(request, dato_usuario_nav):
#     return HttpResponse("Estas mirando la pregunta numero: %s." % dato_usuario_nav)
#Es importante usar los formatos "%s" y "%" para que funcione bien

def results(request, dato_usuario_nav):
    response = "Y Estas mirando los resultados de la pregunta %s."
    return HttpResponse(response % dato_usuario_nav)


# def vote(request, dato_usuario_nav):
#     return HttpResponse("Tu voto en la pregunta es de: %s." % dato_usuario_nav)


def vote(request, dato_usuario_nav):
    pregunta = get_object_or_404(Question, pk=dato_usuario_nav)
    try: #request.POST es un diccionario que permite acceder a datos que han enviado mediante su nombre clave "Choice" en este caso
         # Tambien existe  request.GET para acceder a los datos GET
        respuesta_seleccionada = pregunta.Foranea_pregunta.get(pk=request.POST["choice"]) 
    
    except (KeyError, Choice.DoesNotExist): #Se da KeyError cuando no se encuentra una clave en un diccionario, muestra el formulario de nuevo con un mensaje de error
        return render(
            request,
            "polls/detail.html",
            {
                "question": pregunta,
                "error_message": "DEBES SELECCIONAR UNA OPCION",
            },
        )
    
    else:
        respuesta_seleccionada.votes = F("votes") + 1 #F nos sirve para para acceder directamente a la base de datos y hacer la modificacion, en este caso por cada que se seleccione el campo ratio se añade un voto, posterior a ESO SE TIENE QUE GUARDAR
        respuesta_seleccionada.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        #Posterior a guardar el voto se redirije al usuario a la vista resultados de la encuesta
        return HttpResponseRedirect(reverse("polls:results", args=(pregunta.id,)))

#Una vista puede hacer 2 cosas, o devolver un HttpResponse con el contenido HTML que queremos ver o hacer un excepcion con Http404

#Comentamos la vista index y creamos una nueva, esta lo que hace es mostrarnos todos los objetos del modelo Questions odenado por fecha de publicacion separados por , 

# def index(request):
#     ultimas_preguntas_hechas = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in ultimas_preguntas_hechas])
#     return HttpResponse(output)

#Funciona correctamente pero no es lo correcto codificar el diseño de pagina desde codigo de py, lo mejor es usar el sistema de plantillas 

#Creamos un directorio "templates" Django siempre buscara las plantillas ahi

#Esta vendria a ser la funcion de vista usada para la plantilla
# def index(request):
#     ultimas_preguntas_hechas = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "ultimas_preguntas_hechas": ultimas_preguntas_hechas,
#     }
#     return HttpResponse(template.render(context, request))

#Este codigo carga la platilla polls/index.html, contexto es un diccionario que mapea nombres de variables de plantilla a objetos

def index(request):
    ultimas_preguntas_hechas = Question.objects.order_by("-pub_date")[:5]
    context = {"ultimas_preguntas_hechas": ultimas_preguntas_hechas}
    return render(request, "polls/index.html", context)

#Creamos una funcion index que hace lo mismo que la anterior, solo que simplifica un poco el proceso usando render  

#Ahora lo idea seria meter una excepcion para cuando arroje un error 404, en este caso vamos a reestructurar la vista detail

# def detail(request, dato_usuario_nav):
#     try:
#         pregunta = Question.objects.get(pk=dato_usuario_nav)
#     except Question.DoesNotExist:
#         raise Http404("No existe tu pregunta BB :(")
#     return render(request, "polls/detail.html", {"question": pregunta})

#En este caso la excepcion dara su aparicion cuando no se encuentre una pregunta con el ID solicitado

#El codigo anterior funciona bien pero lo podemos simpleficar aun mas con la funcion get_object_or_404, nos ahorramos el try y except

def detail(request, dato_usuario_nav):
    pregunta = get_object_or_404(Question, pk=dato_usuario_nav)
    return render(request, "polls/detail.html", {"question": pregunta})

#hay una funcion get_list_or_404 que devuelve Http404 si la lista esta vacia