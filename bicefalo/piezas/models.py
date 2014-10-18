#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from countries.models import Country


class Autor(models.Model):
    pais = models.ForeignKey(Country, related_name='autores')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
    class Meta:
        db_table='Autor'
        verbose_name='autor'
        verbose_name_plural='autores'
        
    def __unicode__(self):
        return self.nombre + ' ' + self.apellido
    
    
class Pieza(models.Model):
    from usuarios.models import Perfil
    prepopulated_fields = {'slug':('codigoSlug',)}
    #Definicion de campos
    codigo = models.CharField(primary_key=True, max_length=20)
    codigoSlug = models.SlugField(blank=True)
    clasificacion = models.ForeignKey('Clasificacion', related_name='piezas')
    autor = models.ForeignKey(Autor, blank=True, null=True, related_name='creaciones')
    responsableRegistro = models.ForeignKey(Perfil, related_name='piezas_registradas')
    registroIDAEH = models.BooleanField(default=False, blank=True)
    codigoIDAEH = models.CharField(max_length=25, blank=True, null=False)
    archivoIDAEH = models.FileField(blank=True, null=True, upload_to="files")
    nombre = models.CharField(max_length=140, blank=True)
    descripcion = models.TextField()
    fechaIngreso = models.DateField(auto_now=True)
    procedencia = models.CharField(max_length=50, blank=True)
    pais = models.ForeignKey(Country, blank=True, null=True, related_name='piezas')
    regionCultural = models.SmallIntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True)
    maestra = models.BooleanField(default=False, blank=True)
    exhibicion = models.BooleanField(default=False, blank =True)
    altura = models.FloatField(blank=True, null=True)
    ancho = models.FloatField(blank=True, null=True)
    grosor = models.FloatField(blank=True, null=True)
    largo = models.FloatField(blank=True, null=True)
    diametro = models.FloatField(blank=True, null=True)
    
    class Meta:
        db_table='Pieza'
        verbose_name='pieza'
        verbose_name_plural='piezas'
    
    def __unicode__(self):
        return self.codigo

class Fotografia(models.Model):
    from operaciones.models import Mantenimiento
    mantenimiento = models.ForeignKey(Mantenimiento, blank=True, related_name='mantenimiento')
    pieza = models.ForeignKey(Pieza, blank=True, null=True)
    tipo = models.SmallIntegerField(blank=True)
    ruta = models.ImageField(upload_to='piezas')
    perfil = models.BooleanField(default=True)
    
    class Meta:
        db_table='Fotografia'
        verbose_name='fotografía'
        verbose_name_plural='fotografías'
        
class Clasificacion(models.Model):
    from registro.models import Ficha
    from colecciones.models import Coleccion, Categoria
    coleccion = models.ForeignKey(Coleccion, related_name="clasificaciones")
    categoria = models.ForeignKey(Categoria, related_name="clasificaciones")
    ficha = models.ForeignKey(Ficha, related_name="clasificaciones")
    nombre = models.CharField(max_length=50, null=False)
    codigo = models.CharField(max_length=50, unique=True)
    
    class Meta:
        db_table='Clasificacion'
        verbose_name='clasificación'
        verbose_name_plural = 'clasificaciones'
        
    def __unicode__(self):
        return self.nombre