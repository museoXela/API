#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
        
    class Meta:       
        db_table='Categoria'
        verbose_name='categoría'
        verbose_name_plural='categorías'
        
    def __unicode__(self):
        return self.nombre

class Coleccion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    class Meta:
        db_table='Coleccion'
        verbose_name='Colección'
        verbose_name_plural='Colecciones'  
              
    def __unicode__(self):
        return self.nombre