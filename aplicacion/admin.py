from django.contrib import admin

# Register your models here.

from .models import Aprendiz,Calificaciones,Competencias
admin.site.register(Aprendiz)
admin.site.register(Calificaciones)
admin.site.register(Competencias)