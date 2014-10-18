from __future__ import unicode_literals
from bicefalo.utils import CustomResource
from models import Traslado, Caja, Sala, Vitrina
class Traslado(CustomResource):
    class Meta:
        queryset= Traslado.objects.all()
        resource_name= 'traslados'
    
class Caja(CustomResource):
    class Meta:
        queryset= Caja.objects.all()
        resource_name= 'cajas'

class Sala(CustomResource):
    class Meta:
        queryset= Sala.objects.all()
        resource_name= 'salas'
        fields=['nombre', 'descripcion','fotografia']
class Vitrina(CustomResource):
    class Meta:
        queryset= Vitrina.objects.all()
        resource_name= 'vitrina'
enabled_resources=[Traslado,Caja, Sala, Vitrina]