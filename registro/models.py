#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

class Ficha(models.Model):
    nombre = models.CharField(unique=True,max_length=50)
    estructura = models.TextField()
    consolidacion = models.BooleanField(default=False)
    
    class Meta:
        db_table='Ficha'
        verbose_name='ficha de registro'
        verbose_name_plural='fichas de registro'
        
    def __unicode__(self):
        return self.nombre
    
class Registro(models.Model):
    from operaciones.models import Consolidacion
    from piezas.models import Pieza
    registroPieza = models.ForeignKey(Pieza,blank=True, related_name='registro')
    registroConsolidacion = models.ForeignKey(Consolidacion, blank=True, related_name='registro')
    fecha = models.DateField(auto_now=True)
    consolidacion = models.BooleanField(default=False)

    class Meta:
        db_table='Registro'
        verbose_name='registro de pieza'
        verbose_name='registro de piezas'
        
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
    
    class Meta:
        db_table='Campo'
        verbose_name='campo de registro'
        verbose_name_plural='campos de registro'
        
    def __unicode__(self):
        return self.registro + ' -detalle- ' + unicode(self.campoEstructura)
    
class ValorCheck(models.Model):
    campo = models.ForeignKey('Campo',related_name='valorCheck')
    nombre = models.CharField(max_length=45)
    seleccionado = models.BooleanField(default=False)
    
    class Meta:
        db_table='ValorCheck'
        verbose_name='campo de valor múltiple'
        verbose_name_plural='campos de valor múltiple'
    def __unicode__(self):
        return unicode(self.nombre)
