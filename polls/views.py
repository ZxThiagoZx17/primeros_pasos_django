from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.

#Creamos una vista simple en django, ahora tenemos que definirle una url
# def index(request):
#     return HttpResponse("Hola bebe este es el index request")

#Definimos las vistas para mostrar como podemos anexar datos que ingrese el usuario en la url en la pagina principal
# def detail(request, dato_usuario_nav):
#     return HttpResponse("Estas mirando la pregunta numero: %s." % dato_usuario_nav)
#Es importante usar los formatos "%s" y "%" para que funcione bien

# def results(request, dato_usuario_nav):
#     response = "Y Estas mirando los resultados de la pregunta %s."
#     return HttpResponse(response % dato_usuario_nav)

# def results(request, dato_usuario_nav):
#     pregunta = get_object_or_404(Question, pk=dato_usuario_nav)
#     return render(request, "polls/results.html", {"question": pregunta})

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

# def index(request):
#     ultimas_preguntas_hechas = Question.objects.order_by("-pub_date")[:5]
#     context = {"ultimas_preguntas_hechas": ultimas_preguntas_hechas}
#     return render(request, "polls/index.html", context)

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

# def detail(request, dato_usuario_nav):
#     pregunta = get_object_or_404(Question, pk=dato_usuario_nav)
#     return render(request, "polls/detail.html", {"question": pregunta})

#hay una funcion get_list_or_404 que devuelve Http404 si la lista esta vacia

#Django tiene un paquete de vistas genericas ya que hay muchos patrones de diseño que son similires como recopilar datos de la bd y devolver una lista, para renovar nuestro codigo y simplificar haremos lo siguiente:
    # Convierte el URLconf.
    # Elimine algunas de las vistas antiguas e innecesarias.
    # Introduzca nuevas vistas basadas en vistas genéricas de Djangoangs.

# Una vez modificado urls.py comentamos las vistas viejas y creamos las nuevas:

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "ultimas_preguntas_hechas" #Varible donde se establece como se llama a la lista de elementos en la plantilla, object_list es por defecto si este no se define

    def get_queryset(self): #Este metodo mos sirve para definir los elementos que queremos mostrar o limitarlos en cantidad
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    #Modificamos get_queryset para que solo devuelva preguntas con pub_date anteriores a ahora, osea que no esten en futuro

#Este es el modelo basico en detailview, simplemente definimos el modelo y accedemos a atributos mediante el mediante .

class DetailView(generic.DetailView):
    model = Question                
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

#Django proporciona unmodulo Client para simular un usuario en el codigo a nivel de vistas, se puede usar con test.py o shell:

"""
from django.test.utils import setup_test_environment
setup_test_environment()
"""

#setup_test_environment() instala un renderizador de plantillas que nos permitira examinar atributos en las respuestas como response.context, en este caso TIME_ZONE en settings.py debe estar configurado para evitar inconsistencias, luego importamos django.test.Client y lo instanciamos, con este simulamos la interaccion del usuario

"""
 from django.test import Client
 # create an instance of the client for our use
 client = Client()
"""

#A continuacion se mostraran ejemplos de como extraer informacion de la solicitud HTTP
"""
# Obtener respuesta de '/'
response = client.get("/")
Not Found: /

# Debemos esperar un 404 debido a la direccion; si vemos un error de 
# "Encabezado HTTP_HOST no válido" y una respuesta 400, es posible
# que se haya omitido la llamada a setup_test_environment() 
response.status_code
404

#Por el lado de /Polls/ podemos encontrar algo, usaremos reverse() en lugar
# de la url codificada 
from django.urls import reverse
response = client.get(reverse("polls:index"))
response.status_code
200

response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>
"""

