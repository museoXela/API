from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from models import Traslado, Caja, Sala, Vitrina
class Traslado(CustomResource):
    class Meta:
        queryset= Traslado.objects.all()
        resource_name= 'traslados'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    
class Caja(CustomResource):
    class Meta:
        queryset= Caja.objects.all()
        resource_name= 'cajas'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

class Sala(CustomResource):
    class Meta:
        queryset= Sala.objects.all()
        resource_name= 'salas'
        fields=['nombre', 'descripcion','fotografia']      
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
class Vitrina(CustomResource):
    class Meta:
        queryset= Vitrina.objects.all()
        resource_name= 'vitrina'
        allowed_methods=['get','post','put']       
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
enabled_resources=[Traslado,Caja, Sala, Vitrina]