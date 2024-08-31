import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionModelosTesteo(TestCase):
    def test_was_published_recently_futuro(self):
        """
        was_published_recently() devuelve False para pub_date en fechas futuras a la actual
        """
        time = timezone.now() + datetime.timedelta(days=30)
        pregunta_futura = Question(pub_date=time)
        #assertIs() comprueba 2 resultados sean iguales, en este caso el resultado de was_published_recently() con False
        self.assertIs(pregunta_futura.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() Devuelve False para fechas de publicacion
        inferiores a 1 dia.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() Devuelve True para fechas de publiacion
        dentro del mismo dia.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

# Ejecutamos pruebas con el comando $ python manage.py test polls

# En nuestro caso debe fallar debido a lo que explicamos anteriormente, si usamos git hub accions nos dara error en el WorkFlow

#El codigo hizo lo siguiente:
"""
1. python manage.py test polls Busca test.py en la carpeta de la aplicacion
2. Encontro una subclase django.test.TestCase 
3. Creo una base de datos para pruebas 
4. Busca metodos de prueba que comiencen con el nombre "test" ---> test_was_published_recently_futuro
5. Dentro de este metodo se crea una instancia de Question con un tiempo que va de hoy a 30 dias en el futuro
6. Finalmente assertIs() comprueba 2 resultados sean iguales, en este caso el resultado de was_published_recently() con False
"""

#Modificamos la funcion was_published_recently() para que funcione de acuerdo a como la necesitamos, corremos de nuevo test y funciona bien

#Creamos otras 2 funciones de test para comprobar mas posibles casos de error test_was_published_recently_with_recent_question y test_was_published_recently_with_old_question


def create_question(question_text, days):
    """
    Se encarga de crear preguntas o instancias de la clase Question con el "question_text"
    Indicado en los argumentos, tambien admite un numero de dias que segun sea negativo o
    positivo la pub_date sera en pasado o futuro
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        Si no existen preguntas, que se muestre el mensaje apropiado
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay preguntas creadas")
        self.assertQuerySetEqual(response.context["ultimas_preguntas_hechas"], []) #Verifica que response.context["ultimas_preguntas_hechas"] nos  devuelva []

    def test_past_question(self):
        """
        Las preguntas con pub_date anterior a ahora se mostraran en la 
        pagina indice
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["ultimas_preguntas_hechas"],[question],
            #Verifica que la lista retorne la pregunta con pub_date anterior a ahora, cabe recalcar que en esa lista unicamente apareceran preguntas creadas dentro de la misma prueba
        )

    def test_future_question(self):
        """
        Las preguntas con pub_date Despues a ahora NO se mostraran en la 
        pagina indice
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No hay preguntas creadas")
        self.assertQuerySetEqual(response.context["ultimas_preguntas_hechas"], [])

    def test_future_question_and_past_question(self):
        """
        Incluso si se crean preguntas en pasado y futuro, unicamente se mostraran
        las que estan en pasado.
        """
        question = create_question(question_text="Past question.", days=-30)#Unicamente se guarda en variable para compararla mas adelante
        create_question(question_text="Future question.", days=30)#Esta pregunta se guarda en la base de datos temporal de pruebas
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["ultimas_preguntas_hechas"],
            [question],
        )

    def test_two_past_questions(self):
        """
        Se muestran varias preguntas creadas en pasado
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["ultimas_preguntas_hechas"],
            [question2, question1],
        )

#TODOS ESTOS METODOS ANTERIORES SON PARA LA VISTA INDEX, DE AHI EL NOMBRE DE LA CLASE QuestionIndexViewTests

#Las pruebas que tenemos estan bien, sin embargo, si los ususarios adivinan la URL Pueden llegar a las preguntas futuras para votar en detail.html, por lo tanto debemos agregar una restriccion similar a DetailView en views.py

#Test para Detail.html
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        Si la pregunta tiene un pub_date mayor a ahora, devolvera un 404
        al poner la id del objeto en la URL
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        Si la pregunta tiene un pub_date menor a ahora, devolvera el formulario
        al poner la id del objeto en la URL.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)