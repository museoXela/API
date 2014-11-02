from django.db import models
#esto es para agregar eso from usuario.models import Perfil
# Create your models here.
#Victor 
class Traslado (models.Model):
	from usuarios.models import Perfil
	from piezas.models import Pieza
	fecha= models.DateField(auto_now=True,blank=True,null=True)
	bodega=models.BooleanField(default=True,blank=True)
	caja= models.ForeignKey('Caja', blank=True, null=True)
	vitrina=models.ForeignKey('Vitrina', blank=True, null=True)
	responsable=models.ForeignKey(Perfil) 
	pieza=models.ForeignKey(Pieza) 
	
	class Meta:
		db_table='Traslado'
		verbose_name='traslado'
		verbose_name_plural='traslados'
		def __unicode__(self):
			return self.fecha 
	
class Caja(models.Model):
	codigo= models.CharField(unique=True, null=True,blank=True,max_length=50)
	class Meta:
		db_table='Caja'
		verbose_name='caja'
		verbose_name_plural='cajas'
	def __unicode__(self):
		return self.codigo 
	
class Sala(models.Model):
	nombre=models.CharField(unique=True,null=True,blank=True,max_length=50)
	descripcion=models.TextField(null=True,blank=True,max_length=50)
	fotografia=models.URLField(null=True,blank=True)
	class Meta:
		db_table='Sala'
		verbose_name='sala'
		verbose_name_plural='salas'
	def __unicode__(self):
		return self.nombre
	
class Vitrina(models.Model):
	numero=models.CharField(null=True,blank=True, max_length=20)
	sala = models.ForeignKey(Sala)
	class Meta:
		db_table='Vitrina'
		verbose_name='vitrina'
		verbose_name_plural='vitrinas'
		def __unicode__(self):
			return self.numero
