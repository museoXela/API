from bicefalo.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from models import Pieza
from models import Autor
from models import Fotografia
from models import Clasificacion

# Create your views here.

class Pieza (ModelResource):
    class Meta:
        queryset = Pieza.objects.all()
        resource_name='piezas'
        allowed_methods = ['get','put','post']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]

class Autor (ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        resource_name='autor'
        allowed_methods = ['get','put','post']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
    
class Fotografia (ModelResource):
    class Meta:
        queryset = Fotografia.objects.all()
        resource_name='fotografia'
        allowed_methods = ['get','put','post']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
    
class Clasificacion (ModelResource):
    class Meta:
        queryset = Clasificacion.objects.all()
        resource_name='clasificacion'
        allowed_methods = ['get','put','post']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]