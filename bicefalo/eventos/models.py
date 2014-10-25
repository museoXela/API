from django.db import models
#esto es para agregar eso from usuario.models import Perfil
# Create your models here.
class Eventos (models.Model):
    from traslados.models import Sala
    from usuarios.models import Perfil
    nombre = models.CharField(unique=True, null=True,blank=True,max_length=45)
    descripcion=models.TextField(null=True,blank=True)
    afiche =models.ImageField(null=True,blank=True, upload_to='afiches')
    fecha=models.DateField(blank=True, null=True)
    sala=models.ForeignKey(Sala)
    usuario =models.ForeignKey(Perfil)
    hora = models.TimeField(null=True)
    class Meta:
        db_table='Eventos'
        verbose_name='evento'
        verbose_name_plural='eventos'
        
    def __unicode__(self):
        return self.nombre 