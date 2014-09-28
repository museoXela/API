from django.db import models
from piezas.models import Autor, Pieza
from usuarios.models import Perfil

class Investigacion(models.Model):
    editor = models.ForeignKey(Perfil)
    titulo = models.CharField(max_length=45)
    contenido = models.TextField()
    resumen = models.CharField(max_length=140, blank=True)
    autor = models.ForeignKey(Autor, related_name='investigaciones')
    fecha = models.DateField(auto_now = True)
    publicado = models.BooleanField(default=True)
    piezas = models.ManyToManyField(Pieza, related_name='investigaciones')
    def __unicode__(self):
        return unicode(self.editor) + '-' + unicode(self.titulo)

class LinkInvestigacion(models.Model):
    investigacion = models.ForeignKey(Investigacion)
    link = models.URLField()
    
    def __unicode__(self):
        return unicode(self.link)