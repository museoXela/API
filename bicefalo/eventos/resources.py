from __future__ import unicode_literals
from bicefalo.utils import CustomResource
from models import Eventos

class Eventos(CustomResource):
    class Meta:
        queryset= Eventos.objects.all()
        resource_name= 'eventos'
enabled_resources=[Eventos]