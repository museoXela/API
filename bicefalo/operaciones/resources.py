from bicefalo.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie import fields
#from operaciones.models import Mantenimiento
#from operaciones.models import Consolidacion
class Mantenimiento(ModelResource):
	class Meta:
		queryset= Mantenimiento.objects.all()
		resource_name= 'mantenimiento'
		allowed_methods=['get','post','put']
		authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
		
class Consolidacion(ModelResource):
	class Meta:
		queryset= Consolidacion.objects.all()
		resource_name= 'consolidacion'
		allowed_methods=['get','post','put']
		authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
	
# Create your views here.
