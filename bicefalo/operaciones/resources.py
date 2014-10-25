from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from models import Mantenimiento, Consolidacion
class Mantenimiento(CustomResource):
	class Meta:
		queryset= Mantenimiento.objects.all()
		resource_name= 'mantenimiento'
		allowed_methods=['get','post','put']
		authorization = DjangoAuthorization()
		authentication = OAuth20Authentication()
		
class Consolidacion(CustomResource):
	class Meta:
		queryset= Consolidacion.objects.all()
		resource_name= 'consolidacion'
		allowed_methods=['get','post','put']
		authorization = DjangoAuthorization()
		authentication = OAuth20Authentication()
		
enabled_resources=[Mantenimiento,Consolidacion]