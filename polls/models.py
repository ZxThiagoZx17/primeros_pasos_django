#Este modulo es una fuente de informacion en la que se definen los modelos de datos (tablas) en SQL 
from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin #Decorador para usar display()

# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")
    
#     def __str__(self):
#         return self.question_text

#     #Funcion que establece una diferencia en el tiempo que se creo la instancia y el ahora para devolver True si se creo recientemente o False de o contrario 
#     def was_published_recently(self):
#         Ahora = timezone.now()
#         return Ahora - datetime.timedelta(days=1) <= self.pub_date <= Ahora
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        Ahora = timezone.now()
        return Ahora - datetime.timedelta(days=1) <= self.pub_date <= Ahora
# Modelo para mejorar la apariencia en el panel de administracion de DJANGO

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='Foranea_pregunta')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

#__str__ para la representacion de nuestros objetos
    def __str__(self):
        return self.choice_text
#Cada modelo usa una subclase django.db.models.Model que nos ayuda a representar el tipo de instacia

#Una vez creado lo agragamos a Settings en INSTALLED_APPS y corremos makemigrations, esto le dira a DJANGO que hemos creado nuevos modelos

#Se guardara en migrations el codigo Django que ejecuta la consulta en SQL, si queremos mirar como es el lenguaje SQL usado usaremos el comando py manage.py sqlmigrate polls 0001 para este caso:

"""
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
"""

#La salida varia segun la base de datos que estemos usando, una vez comprobado se usa migrate para modificar la base de datos

"""
Cambia tus modelos (en models.py).
Correr para crear migraciones para esos cambiospython manage.py makemigrations
Correr para aplicar esos cambios a la base de datos.python manage.py migrate
"""

#Podemos interactuar con la shell de django py manage.py shell, podemos modificar instancias desde ahi

"""
from polls.models import Choice, Question
Question.objects.all()
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith="que")

Algunos comandos para probar en shell y mirar instancias, obviamente se deben crear previamente 
https://docs.djangoproject.com/en/5.1/intro/tutorial02/ pagina donde explica con claridad
"""

#Las pruebas son una parte fundamental en nuestro codigo, nos ayuda a identificar errores actualmente y a futuro, aca por ejemplo tenemos un pequeño error en la funcion Question.was_published_recently(), Devuelve True si la fecha de publicacion es en el futuro:

"""
$  python manage.py shell

>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True
"""

# Para hacer la prueba de manera automatizada creamos el archivo tests.py 

# Podemos mejorar aun mas el estilo en el panel de administracion de Django con display() 

# Se deja en las lineas de arriba

