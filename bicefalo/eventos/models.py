from django.db import models
from datetime import date
class Eventos (models.Model):
    from traslados.models import Sala
    from usuarios.models import Perfil
    nombre = models.CharField(unique=True, null=True,blank=True,max_length=45)
    descripcion=models.TextField(null=True,blank=True)
    afiche =models.URLField(null=True,blank=True)
    fecha=models.DateField(blank=True, null=True)
    sala=models.ForeignKey(Sala)
    usuario =models.ForeignKey(Perfil)
    hora = models.TimeField(null=True)
    class Meta:
        db_table='Eventos'
        verbose_name='evento'
        verbose_name_plural='eventos'
    def get_statistics(self):
        eventos = {}
        eventos['pasados'] = Eventos.objects.filter(fecha__lt=date.today()).count()
        eventos['futuros'] = Eventos.objects.filter(fecha__gte=date.today()).count()
        eventos['hoy']= Eventos.objects.filter(fecha=date.today()).count()
        return eventos
    def __unicode__(self):
        return self.nombre 