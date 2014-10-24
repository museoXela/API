from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from models import Eventos
import datetime

class EventosResource(CustomResource):
    sala = fields.CharField(attribute='sala')
    fotoSala = fields.CharField(null=True)
    usuario = fields.CharField(attribute='usuario')
    class Meta:
        queryset=  Eventos.objects.all()
        resource_name= 'eventos'
        excludes=['id']
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    def dehydrate_fotoSala(self, bundle):
        return unicode(bundle.obj.sala.fotografia)
        
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
    
class EventosRecientes(EventosResource):
    class Meta:
        queryset=  Eventos.objects.filter(fecha__gte=datetime.date.today()).order_by('-fecha')
        resource_name= 'eventos'
        excludes=['id']
        allowed_methods=['get']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
enabled_resources=[EventosResource]
web_resources=[EventosRecientes]