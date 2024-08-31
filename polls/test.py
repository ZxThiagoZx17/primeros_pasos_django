import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelosTesteo(TestCase):
    def test_was_published_recently_futuro(self):
        """
        was_published_recently() devuelve False para pub_date en fechas fururas a la actual
        """
        time = timezone.now() + datetime.timedelta(days=30)
        pregunta_futura = Question(pub_date=time)
        #assertIs() comprueba 2 resultados sean iguales, en este caso el resultado de was_published_recently() con False
        self.assertIs(pregunta_futura.was_published_recently(), False)