from django.db import models
from registro.models import Ficha

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)    
    def __unicode__(self):
        return self.nombre

class Coleccion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)    
    def __unicode__(self):
        return self.nombre
    
class Clasificacion(models.Model):
    coleccion = models.ForeignKey(Coleccion, related_name="clasificaciones")
    categoria = models.ForeignKey(Categoria, related_name="clasificaciones")
    ficha = models.ForeignKey(Ficha, related_name="clasificaciones")
    nombre = models.CharField(max_length=50,null=False)
    codigo = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.nombre