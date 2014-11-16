from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from models import Ficha, Registro, Campo, ValorCheck

class Ficha(CustomResource):
    estructura = fields.DictField(attribute='estructura')
    class Meta:
        queryset = Ficha.objects.all()
        resource_name='fichas'
        fields=['id','nombre','consolidacion']
        allowed_methods=['get','post','put','delete']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

class RegistroResource(CustomResource):
    class Meta:
        queryset=Registro.objects.all()
        allowed_methods=['get','post', 'put']
        resource_name='registro'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        exclude = ['id']
        include_resource_uri=False
        
class CamposResource(CustomResource):
    class Meta:
        queryset=Campo.objects.all()
        allowed_methods=['get', 'post', 'put']
        resource_name='campos'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        exclude = ['id']
        include_resource_uri=False
         
class CheckResource(CustomResource):
    class Meta:
        queryset=ValorCheck.objects.all()
        allowed_methods=['get', 'post', 'put']
        resource_name='multiple_choice'
        authorization = DjangoAuthorization()
        authentication =OAuth20Authentication()
        exclude=['id']
        include_resource_uri=False

enabled_resources=[Ficha, RegistroResource]