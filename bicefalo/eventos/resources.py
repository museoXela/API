from bicefalo.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource

class Eventos(ModelResource):
    class Meta:
        queryset= Eventos.objects.all()
        resource_name= 'eventos'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
# Create your views here.
