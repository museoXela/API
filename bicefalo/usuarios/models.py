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
    class Meta:
        db_table='UserDetail'
        verbose_name='perfil'
        verbose_name_plural='perfiles'
          
    usuario = models.OneToOneField(User, related_name='profile')
    pais = models.ForeignKey(Country,  null=True)
    fotografia = models.ImageField(upload_to="users", null=True, blank=True,
                                default='users/default.png')    
    followers = models.ManyToManyField(User, related_name='followers', null=True, blank=True)
    followings = models.ManyToManyField(User, related_name='followings', null=True, blank=True)
    
    def __unicode__(self):
        return self.usuario.get_username()
    
class Publicacion(models.Model):
    autor = models.ForeignKey(Perfil, related_name='publicaciones')
    fecha = models.DateField(auto_now=True, blank=True, null=True)
    nombre = models.CharField(max_length=140)
    publicacion = models.CharField(max_length=200)
    link = models.URLField()
    
    class Meta:
        db_table='Publicacion'
        verbose_name='publicación'
        verbose_name_plural='publicaciones'  
          
    def __unicode__(self):
        return self.nombre