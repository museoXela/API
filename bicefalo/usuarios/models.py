# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from countries.models import Country
from django.dispatch import receiver

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
          
    usuario = models.OneToOneField(User, related_name='perfil')
    filiacionAcademica = models.CharField(blank=True, max_length=50)
    pais = models.ForeignKey(Country,  blank=True, null=True)
    fotografia = models.URLField(null=True, blank=True)
    biografia = models.TextField(blank = True)
    voluntario = models.BooleanField(default=False)
    def __unicode__(self):
        return self.usuario.get_username()
    
    def get_statistics(self):
        usuarios = {}
        usuarios['registrados'] = User.objects.count()
        usuarios['voluntarios'] = Perfil.objects.filter(voluntario=True).count()
        return usuarios
    
@receiver(post_save,sender = User)
def create_profile(sender, **kwargs):
    user = kwargs.get('instance')
    if kwargs.get('created', False):
        Perfil.objects.create(usuario=kwargs.get('instance'), pais=None)
    elif user.perfil:
        user.perfil.save()
        
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
