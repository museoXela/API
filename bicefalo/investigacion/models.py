#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from piezas.models import Autor, Pieza
from usuarios.models import Perfil
import datetime
class Investigacion(models.Model):
    editor = models.ForeignKey(Perfil, related_name='investigaciones')
    titulo = models.CharField(max_length=45)
    contenido = models.TextField()
    resumen = models.CharField(max_length=140, blank=True)
    autor = models.ForeignKey(Autor, related_name='investigaciones')
    fecha = models.DateField(default=datetime.date.today())
    publicado = models.BooleanField(default=True)
    piezas = models.ManyToManyField(Pieza, related_name='investigaciones')
    
    class Meta:
        db_table='Investigacion'
        verbose_name='Investigación'
        verbose_name_plural= 'Investigaciones'
        
    def __unicode__(self):
        return unicode(self.editor) + '-' + unicode(self.titulo)   
    
    def get_statistics(self):
        dict = {}
        dict['investigaciones']=Investigacion.objects.count()
        dict['publicadas']=Investigacion.objects.filter(publicado=True).count()
        dict['borradores']=Investigacion.objects.filter(publicado=False).count()
        return dict
    
class LinkInvestigacion(models.Model):    
    investigacion = models.ForeignKey(Investigacion, related_name='links')
    link = models.URLField()
    class Meta:
        db_table = 'LinkInvestigacion'
        verbose_name = 'link de investigación'
        verbose_name_plural = 'links de investigación'
        
    def __unicode__(self):
        return unicode(self.link)
    
    