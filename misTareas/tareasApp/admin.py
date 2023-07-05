from django.contrib import admin
from tareasApp.models import Etiqueta
# Register your models here.

class Etiquetas_Admin(admin.ModelAdmin):             # Modelo de empresas
    list_display = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']
    fields = ['nombre']

admin.site.register(Etiqueta, Etiquetas_Admin)