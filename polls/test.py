import datetime

from django.test import TestCase
from django.utils import timezone

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