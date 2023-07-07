from django.contrib import admin
from tareasApp.models import Etiqueta, Estado, Tarea
# Register your models here.

class Etiquetas_Admin(admin.ModelAdmin):             # Admin de etiquetas
    list_display = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']
    fields = ['nombre']

admin.site.register(Etiqueta, Etiquetas_Admin)

class Estado_Admin(admin.ModelAdmin):             # Admin de estados
    list_display = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']
    fields = ['nombre']

admin.site.register(Estado, Estado_Admin)

class Tarea_Admin(admin.ModelAdmin):             # Admin de tareas
    list_display = ['titulo', 'fecha_vencimiento', 'etiqueta', 'estado', 'descripcion']
    search_fields = ['titulo']
    ordering = ['titulo']
    fields = ['usuario', 'titulo', 'descripcion', 'fecha_vencimiento', 'etiqueta', 'estado']

admin.site.register(Tarea, Tarea_Admin)