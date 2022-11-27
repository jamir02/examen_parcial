from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=64, default='')
    apellido = models.CharField(max_length=64, default='')
    codigo_usuario = models.CharField(max_length=64, default='')
    clave = models.CharField(max_length=64, default='')

class tarea(models.Model):
    titulo = models.CharField(max_length=64, default='')
    descripcion = models.CharField(max_length=100, default='')
    fecha_creacion = models.CharField(max_length=64, default='')
    fecha_entrega = models.CharField(max_length=64, default='')
    usuario_designado = models.CharField(max_length=64, default='')