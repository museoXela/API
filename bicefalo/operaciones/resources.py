from __future__ import unicode_literals
from bicefalo.utils import CustomResource
from models import Mantenimiento, Consolidacion
class Mantenimiento(CustomResource):
	class Meta:
		queryset= Mantenimiento.objects.all()
		resource_name= 'mantenimiento'
		
class Consolidacion(CustomResource):
	class Meta:
		queryset= Consolidacion.objects.all()
		resource_name= 'consolidacion'
		
enabled_resources=[Mantenimiento,Consolidacion]