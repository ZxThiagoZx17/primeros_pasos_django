from django.contrib import admin
from .models import Question, Choice
# Register your models here.
# Para hacer que los modelos que acabo de crear en models.py sean editables en el portal de administracion de Django necesito registrarlos en admin.py asi:

# admin.site.register(Question) #Con esta linea Django construye la presentacion del formulario de Question
admin.site.register(Choice)

#El panel de administracion de Django nos permitira usar operaciones CRUD con la base de datos

#Ahora vamos a personalizar el formulario de administracion de Django
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    
admin.site.register(Question, QuestionAdmin)