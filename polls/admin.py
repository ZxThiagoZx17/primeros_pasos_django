from django.contrib import admin
from .models import Question, Choice
# Register your models here.
# Para hacer que los modelos que acabo de crear en models.py sean editables en el portal de administracion de Django necesito registrarlos en admin.py asi:

# admin.site.register(Question) #Con esta linea Django construye la presentacion del formulario de Question
# admin.site.register(Choice)

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

#A continuacion vamos a agregar una linea que nos permita agregar varias choices al la hora de agregar una Question
#Comentamos el register() de choice porque ahora lo haremos dentro de question

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

class ChoiceInline(admin.TabularInline): #TabularInline nos sirve para tabular de mejor manera el area para agregar choices
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Infromatiosn de fechaison", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline] #Se añade esta para que Choice se pueda crear dentro de Question

admin.site.register(Question, QuestionAdmin)
