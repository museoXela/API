from django.db import models
#esto es para agregar eso from usuario.models import Perfil
# Create your models here.
class Eventos (models.Model):
    from traslados.models import Sala
    from usuarios.models import Perfil
    nombre = models.TextField(null=True,blank=True)
    descripcion=models.TextField(null=True,blank=True)
    afiche =models.TextField(null=True,blank=True)
    fecha=models.DateField(auto_now=True, blank=True, null=True)
    sala=models.ForeignKey(Sala)
    usuario =models.ForeignKey(Perfil)
    
    class Meta:
        dbTable='Eventos'
        verbose_name='evento'
        verbose_name_plural='eventos'
        
    def __unicode__(self):
        return self.nombre + ' ' + self.descripcion