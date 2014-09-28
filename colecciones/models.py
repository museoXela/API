from django.db import models
    
class Clasificacion(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    codigo = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.nombre