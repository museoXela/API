from django.db import models
#esto es para agregar eso from usuario.models import Perfil
# Create your models here.
class Eventos (models.Model):
    nombre = models.TextField(null=True,blank=True)
    descripcion=models.TextField(null=True,blank=True)
    aficeh =models.TextField(null=True,blank=True)
    fecha=models.DateField(auto_now=True, blank=True, null=True)
    sala=models.ForeignKey('traslados.models.Sala')
    usuario =models.ForeignKey('usuarios.models.Usuario')