from django.db import models
#esto es para agregar eso from usuario.models import Perfil
# Create your models here.
class Traslado (models.Model):
	fecha= models.DateField(auto_now=True,blank=True,null=True)
	bodega=models.BooleanField(null=True,blank=True)
	caja= models.ForeignKey('traslados.models.Caja')
	vitrina=models.ForeignKey('traslados.models.Vitrina')
	responsable=models.ForeignKey('responsables') 
	codigoPieza=models.ForeignKey('codigo pieza') 
class Caja(models.Model):
	codigo= models.TextField(null=True,blank=True)
	
class Sala(models.Model):
	nombre=models.TextField(null=True,blank=True)
	descripcion=models.TextField(null=True,blank=True)
	fotografia=models.TextField(null=True,blank=True)
	
class Vitrina(models.Model):
	numero=models.TextField(null=True,blank=True)
	sala = models.ForeignKey('traslados.models.Sala')
