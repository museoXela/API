from django.db import models
#esto es para agregar eso from usuario.models import Perfil
# Create your models here.
class Traslado (models.Model):
	from usuarios.models import Perfil
	from piezas.models import Pieza
	fecha= models.DateField(auto_now=True,blank=True,null=True)
	bodega=models.BooleanField(null=True,blank=True)
	caja= models.ForeignKey(Caja)
	vitrina=models.ForeignKey(Vitrina)
	responsable=models.ForeignKey('Perfil') 
	codigoPieza=models.ForeignKey('Pieza') 
	class Meta:
        db_table='Traslado'
        verbose_name='traslado'
        verbose_name_plural='traslados'
        
    def __unicode__(self):
        return self.fecha 
	
class Caja(models.Model):
	codigo= models.TextField(null=True,blank=True)
	class Meta:
        db_table='Caja'
        verbose_name='caja'
        verbose_name_plural='cajas'
        
    def __unicode__(self):
        return self.codigo 
	
class Sala(models.Model):
	nombre=models.TextField(null=True,blank=True)
	descripcion=models.TextField(null=True,blank=True)
	fotografia=models.TextField(null=True,blank=True)
	class Meta:
        db_table='Sala'
        verbose_name='sala'
        verbose_name_plural='salas'
        
    def __unicode__(self):
        return self.nombre+' '+self.descripcion 
	
class Vitrina(models.Model):
	numero=models.TextField(null=True,blank=True)
	sala = models.ForeignKey(Sala)
	class Meta:
        db_table='Vitrina'
        verbose_name='vitrina'
        verbose_name_plural='vitrinas'
        
    def __unicode__(self):
        return self.numero
