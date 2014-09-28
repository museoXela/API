from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)    
    def __unicode__(self):
        return self.nombre

class Coleccion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)        
    def __unicode__(self):
        return self.nombre