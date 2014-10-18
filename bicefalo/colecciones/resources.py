from __future__ import unicode_literals
from bicefalo.utils import CustomResource
from models import Categoria, Coleccion

class Categoria(CustomResource):
    class Meta:
        queryset = Categoria.objects.all()
        resource_name='categorias'
        fields = ['nombre']

class Coleccion(CustomResource):
    class Meta:
        queryset = Coleccion.objects.all()
        resource_name='colecciones'
        fields = ['nombre']

enabled_resources=[Categoria,Coleccion]