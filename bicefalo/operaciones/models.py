from django.db import models
#esto es para agregar eso from usuario.models import Perfil
# Create your models here.
class Mantenimiento(models.Model):
	procedimiento = models.IntegerField(null=True, blank=True)
	metodoMaterial = models.TextField(null=True,blank=True)
	fecha = models.DateField(auto_now=True, blank=True, null=True)
	consolidacion = models.ForeignKey('traslados.models.Consolidacion')
	

class Consolidacion(models.Model):
	limpieza= models.BooleanField(default=False)
	fechaInicio = models.DateField(auto_now=True,blank=True,null=True)
	fechaFin = models.DateField(blank=True,null=True)
	responsable=models.ForeignKey('codigo responsable') 
	codigoPieza=models.ForeignKey('codicgo pieza')
	