from django.db import models

class Ficha(models.Model):
    nombre = models.CharField(unique=True,max_length=50)
    estructura = models.TextField()
    consolidacion = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.nombre
    
class Registro(models.Model):
    from operaciones.models import Consolidacion
    from piezas.models import Pieza
    registroPieza = models.ForeignKey(Pieza,blank=True, related_name='registro')
    registroConsolidacion = models.ForeignKey(Consolidacion, blank=True, related_name='registro')
    fecha = models.DateField(auto_now=True)
    consolidacion = models.BooleanField(default=False)

    def __unicode__(self):
        return self.pk + '-' + unicode(self.fecha)

class Campo(models.Model):
    registro = models.ForeignKey('Registro', related_name='detalle')
    campoEstructura= models.IntegerField()
    tipoCampo = models.SmallIntegerField()
    valorTexto = models.CharField(max_length=50, blank=True, null=True)
    valorTextoLargo = models.TextField(blank=True, null=True)
    valorFecha = models.DateField(blank=True, null=True)
    valorNumerico = models.FloatField(blank=True, null=True)
    valorRadio = models.SmallIntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.registro + ' -detalle- ' + unicode(self.campoEstructura)
    
class ValorCheck(models.Model):
    campo = models.ForeignKey('Campo',related_name='valorCheck')
    nombre = models.CharField(max_length=45)
    seleccionado = models.BooleanField(default=False)
