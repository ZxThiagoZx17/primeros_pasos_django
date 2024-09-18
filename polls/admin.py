from django.contrib import admin
from .models import Question, Choice
# Register your models here.
# Para hacer que los modelos que acabo de crear en models.py sean editables en el portal de administracion de Django necesito registrarlos en admin.py asi:

# admin.site.register(Question) #Con esta linea Django construye la presentacion del formulario de Question
admin.site.register(Choice)

#El panel de administracion de Django nos permitira usar operaciones CRUD con la base de datos

#Ahora vamos a personalizar el formulario de administracion de Django

#Con esta linea definimos Este cambio en particular anterior hace que la “Fecha de publicación” venga antes de la “Campo de Question”

#  class QuestionAdmin(admin.ModelAdmin):  
#     fields = ["pub_date", "question_text"]

# Con esta linea dividimos el formulario en conjuntos de campo
# El primer elemento de la tupla "fields" hace referencia al nombre de conjunto de campo
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Infromatiosn de fechaison", {"fields": ["pub_date"]}),
    ]

admin.site.register(Question, QuestionAdmin)
