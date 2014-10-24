from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from models import Categoria, Coleccion

class Categoria(CustomResource):
    class Meta:
        queryset = Categoria.objects.all()
        resource_name='categorias'
        fields = ['nombre']
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

class Coleccion(CustomResource):
    class Meta:
        queryset = Coleccion.objects.all()
        resource_name='colecciones'
        fields = ['nombre']
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

enabled_resources=[Categoria,Coleccion]