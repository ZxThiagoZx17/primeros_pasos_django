from django.contrib import admin
from .models import Question, Choice
# Register your models here.
# Para hacer que los modelos que acabo de crear en models.py sean editables en el portal de administracion de Django necesito registrarlos en admin.py asi:

admin.site.register(Question)
admin.site.register(Choice)

#El panel de administracion de Django nos permitira usar operaciones CRUD con la base de datos