from django.db import models
#esto es para agregar eso from usuario.models import Perfil
# Create your models here.
class Mantenimiento(models.Model):
	procedimiento = models.IntegerField(null=True, blank=True)
	metodoMaterial = models.CharField(null=True,blank=True,max_length=200)
	fecha = models.DateField(blank=True, null=True)
	consolidacion = models.ForeignKey('Consolidacion', related_name='mantenimientos')
	
	class Meta:
		db_table='Mantenimiento'
		verbose_name='mantenimiento'
		verbose_name_plural='mantenimientos'
	def __unicode__(self):
		return self.metodoMaterial + ' ' + self.fecha 
	

class Consolidacion(models.Model):
	from piezas.models import Pieza
	from usuarios.models import Perfil
	limpieza= models.BooleanField(default=False)
	fechaInicio = models.DateField(blank=True,null=True)
	fechaFin = models.DateField(blank=True,null=True)
	responsable=models.ForeignKey(Perfil) 
	pieza=models.ForeignKey(Pieza)
	
	class Meta:
		db_table='Consolidacion'
		verbose_name='consolidacion'
		verbose_name_plural='consolidaciones'
		
	def __unicode__(self):
		return self.limpieza 