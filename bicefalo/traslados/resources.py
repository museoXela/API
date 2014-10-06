from bicefalo.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource

class Traslado(ModelResource):
    class Meta:
        queryset= Traslado.objects.all()
        resource_name= 'traslado'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
    
class Caja(ModelResource):
    class Meta:
        queryset= Caja.objects.all()
        resource_name= 'caja'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
    
class Sala(ModelResource):
    class Meta:
        queryset= Sala.objects.all()
        resource_name= 'sala'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
    
class Vitrina(ModelResource):
    class Meta:
        queryset= Vitrina.objects.all()
        resource_name= 'vitrina'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
# Create your views here.
