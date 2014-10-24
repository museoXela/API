from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from models import Mantenimiento, Consolidacion
class Mantenimiento(CustomResource):
	class Meta:
		queryset= Mantenimiento.objects.all()
		resource_name= 'mantenimiento'
		allowed_methods=['get','post','put']
		always_return_data = False
		authorization = DjangoAuthorization()
		authentication = OAuth20Authentication()
		
class Consolidacion(CustomResource):
	responsable = fields.CharField(attribute='responsable')
	class Meta:
		queryset= Consolidacion.objects.all()
		resource_name= 'consolidacion'
		allowed_methods=['get','post','put']
		always_return_data = False
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
enabled_resources=[Mantenimiento,Consolidacion]