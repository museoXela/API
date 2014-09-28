# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from countries.models import Country

# Create your models here.
class Perfil(models.Model):
    """
    Esta clase representa el modelo de los perfiles que se utilizar�n
    Fecha: 16/10/2013 19:14
    Autor: T4r0_o
    Branch: master
    Modificado: 18/10/2013 
    """
    usuario = models.OneToOneField(User, related_name='perfil')
    pais = models.ForeignKey(Country,  null=True, blank=True, related_name='usuarios')
    fotografia = models.ImageField(upload_to="users", null=True, blank=True,
                                default='users/default.png')
    filiacionAcademica = models.CharField(max_length=50, null= True, blank=True)
    biografia = models.CharField(max_length=140, null=True, blank=True) 

    
    def __unicode__(self):
        return self.usuario.get_username()
    
class Publicacion(models.Model):
    autor = models.ForeignKey(Perfil, related_name='publicaciones')
    fecha = models.DateField(auto_now=True, blank=True, null=True)
    nombre = models.CharField(max_length=140)
    publicacion = models.CharField()
    link = models.URLField()
    
    def __unicode__(self):
        return self.nombre
    