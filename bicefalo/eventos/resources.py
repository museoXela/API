from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from models import Eventos
import datetime

class Eventos(CustomResource):
    sala = fields.CharField(attribute='sala')
    usuario = fields.CharField(attribute='usuario')
    class Meta:
        queryset=  Eventos.objects.filter(fecha__gte=datetime.date.today()).order_by('-fecha')
        resource_name= 'eventos'
        excludes=['id']
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def hydrate_sala(self, bundle):
        from traslados.models import Sala
        sala = bundle.data['sala']
        if sala:
            bundle.data['sala'] = Sala.objects.get(nombre=sala)
        return bundle
    
    def hydrate_usuario(self, bundle):
        from django.contrib.auth.models import User
        from usuarios.models import Perfil
        usuario = bundle.data['usuario']
        if usuario:
            usuario = User.objects.get(username=usuario).perfil
            bundle.data['usuario'] = usuario
        return bundle
        
enabled_resources=[Eventos]