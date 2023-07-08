from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=45, null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

class Estado(models.Model):
    nombre = models.CharField(max_length=45, null=False, blank=False)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE, null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False, blank=False)
    titulo = models.CharField(max_length=45, null=False, blank=False)
    descripcion = models.CharField(max_length=150, null=False, blank=False)
    fecha_vencimiento = models.DateField(default=timezone.now)
    observaciones = models.CharField(max_length=250, null=True, blank=True, default=None)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'