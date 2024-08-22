#Este modulo es una fuente de informacion en la que se definen los modelos de datos (tablas) en SQL 
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

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