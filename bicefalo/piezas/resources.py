#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bicefalo.utils import CustomResource
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from models import Pieza as Piezas, Autor, Fotografia, Clasificacion


# Create your views here.

class Pieza (CustomResource):
    class Meta:
        queryset = Piezas.objects.all()
        resource_name='piezas'
        excludes = ['altura','ancho', 'diametro', 'grosor','largo','codigoSlug']
        filtering = {
                     'fechaIngreso':ALL,
                     'procedencia':ALL,
                     'regionCultural':ALL,
                     'maestra':ALL,
                     'exhibicion':ALL                     
        } 
        
    def dispatch_master(self, request, **kwargs):
        from tastypie.http import HttpMethodNotAllowed
        if request.method == 'GET':
            bundle = self.build_bundle(request=request)
            res = Pieza()
            list = Piezas.objects.filter(maestra=True)
            objects = []
            for piece in list:
                bundle = res.build_bundle(obj=piece, request = request)
                bundle = res.full_dehydrate(bundle)
                del bundle.data['maestra']
                objects.append(bundle)
            res.log_throttled_access(request)
            return res.create_response(request, objects)
        else:
            return self.create_response(request,{'error':'solo se admite el método GET'}, response_class=HttpMethodNotAllowed)
        
    def dispatch_exhibition(self, request, **kwargs):
        from tastypie.http import HttpMethodNotAllowed
        if request.method == 'GET':
            bundle = self.build_bundle(request=request)
            res = Pieza()
            list = Piezas.objects.filter(exhibicion=True)
            objects = []
            for piece in list:
                bundle = res.build_bundle(obj=piece, request = request)
                bundle = res.full_dehydrate(bundle)
                del bundle.data['exhibicion']
                objects.append(bundle)
            res.log_throttled_access(request)
            return res.create_response(request, objects)
        else:
            return self.create_response(request,{'error':'solo se admite el método GET'}, response_class=HttpMethodNotAllowed)
            
    def prepend_urls(self):
        from django.conf.urls import url
        return [
            url(r'^exhibicion/$', self.wrap_view('dispatch_exhibition'), name='exhibition_dispatch'),      
            url(r'^piezas/maestras/$', self.wrap_view('dispatch_master'), name='masterPieces_dispatched'),         
            url(r'^piezas/(?P<pk>\w+)/$', self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),               
            ]

class Autor (CustomResource):
    class Meta:
        queryset = Autor.objects.all()
        resource_name='autores'
    
class Fotografia (CustomResource):
    class Meta:
        queryset = Fotografia.objects.all()
        resource_name='fotografias'
        
class Clasificacion (CustomResource):
    class Meta:
        queryset = Clasificacion.objects.all()
        resource_name='clasificacion'
        
enabled_resources=[Pieza,Autor, Fotografia, Clasificacion]