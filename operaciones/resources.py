from bicefalo.authentication import OAuth20Authentication
from tastypie.resources import ModelResource
from tastypie import fields
from operaciones.models import Mantenimiento
class Mantenimiento(ModelResource):
	class Meta:
		queryset= Mantenimiento.objects.all()
		resource_name= 'mantenimiento'
		allowed_methods=['get','post','put']
# Create your views here.
