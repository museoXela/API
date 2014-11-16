from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie import fields, http
from models import Mantenimiento, Consolidacion
class Mantenimiento(CustomResource):
	consolidacion = fields.IntegerField(attribute='consolidacion_id')
	class Meta:
		queryset= Mantenimiento.objects.all()
		resource_name= 'mantenimiento'
		allowed_methods=['get','post','put','delete']
		always_return_data = True
		authorization = DjangoAuthorization()
		authentication = OAuth20Authentication()
		
class Consolidacion(CustomResource):
	mantenimientos = fields.ToManyField(Mantenimiento, 'mantenimientos', related_name='mantenimientos', full=True)
	responsable = fields.CharField(attribute='responsable')
	pieza = fields.CharField(attribute='pieza_id')
	
	class Meta:
		queryset= Consolidacion.objects.all()
		resource_name= 'consolidacion'
		allowed_methods=['get','post','put', 'delete']
		always_return_data = True
		authorization = DjangoAuthorization()
		authentication = OAuth20Authentication()
	
	def hydrate_responsable(self, bundle):
		from django.contrib.auth.models import User
		from usuarios.models import Perfil
		usuario = bundle.data['responsable']
		if usuario:
			usuario = User.objects.get(username=usuario).perfil
			bundle.data['responsable'] = usuario
		return bundle
	
	def hydrate_pieza(self, bundle):
		from piezas.models import Pieza
		pieza = bundle.data['pieza']
		if pieza:
			pieza = Pieza.objects.get(codigo=pieza)
			bundle.data['pieza'] = pieza
		return bundle
	
enabled_resources=[Mantenimiento,Consolidacion]