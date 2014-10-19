#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ALL
from tastypie import fields
from models import Pieza as Piezas, Autor, Fotografia, Clasificacion


# Create your views here.

class Pieza (CustomResource):
    exclude_master = ['altura','ancho', 'diametro', 'grosor','largo', 'maestra']
    class Meta:
        queryset = Piezas.objects.all()
        resource_name='piezas'
        excludes = ['codigoSlug']
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering = {
                     'fechaIngreso':ALL,
                     'procedencia':ALL,
                     'regionCultural':ALL,
                     'maestra':ALL,
                     'exhibicion':ALL                     
        } 
        
    def dispatch_master(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.throttle_check(request)
        bundle = self.build_bundle(request=request)
        res = Pieza()
        list = Piezas.objects.filter(maestra=True)
        objects = []
        for piece in list:
            bundle = res.build_bundle(obj=piece, request = request)
            bundle = res.full_dehydrate(bundle)
            for field in self.exclude_master:
                del bundle.data[field]
            objects.append(bundle)
        res.log_throttled_access(request)
        return res.create_response(request, objects)
    
    def prepend_urls(self):
        from django.conf.urls import url
        return [    
            url(r'^piezas/maestras/$', self.wrap_view('dispatch_master'), name='masterPieces_dispatched'),         
            url(r'^piezas/(?P<pk>\w+)/$', self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),               
            ]
        
class Exhibicion(CustomResource):
    
    fotografia = fields.CharField(null=True)
    categoria = fields.CharField(null=True)
    class Meta:
        queryset = Piezas.objects.filter(exhibicion=True)
        resource_name = 'exhibicion'
        allowed_methods=['get']
        fields=['nombre', 'descripcion']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def dehydrate_fotografia(self, bundle):
        return bundle.obj.get_profile_image()
    
    def dehydrate_categoria(self, bundle):
        return bundle.obj.get_categoria()
        
class Autor (CustomResource):
    class Meta:
        queryset = Autor.objects.all()
        resource_name='autores'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    
class Fotografia (CustomResource):
    class Meta:
        queryset = Fotografia.objects.all()
        resource_name='fotografias'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
class Clasificacion (CustomResource):
    class Meta:
        queryset = Clasificacion.objects.all()
        resource_name='clasificacion'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
enabled_resources=[Pieza,Autor, Fotografia, Clasificacion, Exhibicion]