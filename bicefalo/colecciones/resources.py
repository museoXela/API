from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from models import Categoria, Coleccion
from tastypie.resources import ALL, ALL_WITH_RELATIONS
class Categoria(CustomResource):
    class Meta:
        queryset = Categoria.objects.all()
        resource_name='categorias'
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering={
                   'nombre':All,}
class Coleccion(CustomResource):
    class Meta:
        queryset = Coleccion.objects.all()
        resource_name='colecciones'
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering={
                   'nombre':All,}

enabled_resources=[Categoria,Coleccion]