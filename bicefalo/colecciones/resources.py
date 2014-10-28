from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from piezas.models import Categoria as Categorias, Coleccion as Colecciones
from tastypie.resources import ALL
class Categoria(CustomResource):
    class Meta:
        queryset = Categorias.objects.all()
        resource_name='categorias'
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering={'nombre':ALL,}
        
    def get_object_list(self, request):
        if request.GET:
            id = request.GET['coleccion']
            if id:
                return Colecciones.objects.get(id=id).categorias.distinct()
        return super(Categoria, self).get_object_list(request)
    
class Coleccion(CustomResource):
    class Meta:
        queryset = Colecciones.objects.all()
        resource_name='colecciones'
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering={
                   'nombre':ALL,}
    

enabled_resources=[Categoria,Coleccion]
web_resources=[Coleccion, Categoria]