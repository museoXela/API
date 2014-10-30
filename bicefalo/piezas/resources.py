#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie import fields, http
from models import Pieza as Piezas, Autor, Fotografia, Clasificacion as Clasificaciones
from tastypie.resources import ObjectDoesNotExist, MultipleObjectsReturned
from tastypie.http import HttpGone, HttpMultipleChoices
from django.conf.urls import url
# Create your views here.

class Pieza (CustomResource):
    exclude_master = ['altura','ancho', 'diametro', 'grosor','largo', 'maestra']
    class Meta:
        queryset = Piezas.objects.all()
        resource_name='piezas'
        excludes = ['codigoSlug']
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering = {
                     'fechaIngreso':ALL,
                     'procedencia':ALL,
                     'regionCultural':ALL,
                     'maestra':ALL,
                     'exhibicion':ALL,
                     'fechamiento':ALL,
                     'clasificacion':ALL,                     
        } 
        
    def get_object_list(self, request):
        import pdb 
        pdb.set_trace()
        if request.GET:
            data = request.GET
            if 'coleccion' in data and 'categoria' in data:
                piezas = Piezas.objects.filter(clasificacion__coleccion=data['coleccion']).filter(clasificacion__categoria=data['categoria'])
                return piezas
            if 'coleccion' in data:
                return Piezas.objects.filter(clasificacion__coleccion=data['coleccion'])            
            if 'categoria' in data:
                return Piezas.objects.filter(clasificacion__categoria=data['categoria'])            
        return super(Pieza, self).get_object_list(request)
    
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
    
        
class Exhibicion(Pieza):
    
    fotografia = fields.CharField(null=True)
    pais= fields.CharField(null=True, attribute='pais')

    class Meta:
        queryset = Piezas.objects.filter(exhibicion=True)
        resource_name = 'exhibicion'
        allowed_methods=['get']
        fields=['codigo','nombre','fechamiento', 'resumen']
        always_return_data = False
        filtering = {
                     'fechaIngreso':ALL,
                     'procedencia':ALL,
                     'regionCultural':ALL,
                     'maestra':ALL,
                     'exhibicion':ALL,
                     'fechamiento':ALL,
                     'clasificacion':ALL,                     
        } 
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_detail_data_to_serialize(self, request, bundle):
        del bundle.data['resumen']
        bundle.data['descripcion'] = unicode(bundle.obj.descripcion)        
        bundle.data['investigaciones'] = self.get_investigaciones_ref(bundle.obj)
        return bundle
    def dehydrate(self, bundle):
        bundle.data['categoria'] = bundle.obj.get_categoria()
        bundle.data['clasificacion'] = bundle.obj.get_clasificacion()
        bundle.data['coleccion'] = bundle.obj.get_coleccion()
        return bundle
    
    def dehydrate_fotografia(self, bundle):
        return bundle.obj.get_profile_image()
    
    def build_filters(self, filters=None):
        if filters is None:
            filters = {}       
        orm_filters = super(Exhibicion, self).build_filters(filters)
        if('categoria' in filters):
            filters['c'] = filters['categoria']        
        if('coleccion' in filters):
            filters['clasificacion__coleccion__id'] = filters['coleccion']    
        return orm_filters
    
    def get_investigaciones_ref(self, obj):
        from investigacion.resources import Investigacion
        from tastypie.utils import trailing_slash
        res = Investigacion()
        list = obj.investigaciones.all()
        objects = []
        for investigacion in list:
            objects.append('/%s/investigaciones/%s%s' %(self.api_name, investigacion.pk, trailing_slash()))
        return objects
    
    def get_investigaciones(self, request, **kwargs):
        from investigacion.resources import Investigacion
        from tastypie.paginator import Paginator
        try:
            bundle = self.build_bundle(data={'codigo':kwargs['codigo']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this uri")
        res= Investigacion()
        objects = []
        list = obj.investigaciones.filter(publicado=True)
        list = Paginator(request.GET, list).page()['objects']
        for obj in list:
            bundle = res.build_bundle(obj=obj, request = request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)
        res.log_throttled_access(request)
        return res.create_response(request, objects)
    
    def get_search(self, request, **kwargs):
        from piezas.models import Pieza 
        from tastypie.paginator import Paginator
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)
        keyword = request.GET['keyword']
        object_list = []
        objects = Pieza.objects.filter(exhibicion=True).filter(nombre__icontains=keyword)
        list = Paginator(request.GET, objects).page()['objects']
        for obj in list:
            bundle = self.build_bundle(obj=obj, request = request)
            bundle = self.full_dehydrate(bundle)
            object_list.append(bundle)
        self.log_throttled_access(request)
        return self.create_response(request, object_list)
    
    def prepend_urls(self):
        from tastypie.utils import trailing_slash
        return [
                url(r'^(?P<resource_name>%s)/buscar%s$' % (self._meta.resource_name,trailing_slash()), self.wrap_view('get_search'), name = 'search'),
                url(r"^(?P<resource_name>%s)/(?P<codigo>\M[\.\d{1,4}]+)/investigaciones/$" % self._meta.resource_name, self.wrap_view('get_investigaciones'), name="dispatch_piezas"),
                url(r"^(?P<resource_name>%s)/(?P<codigo>\M[\.\d{1,4}]+w+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="dispatch_piezas"),
        ]

class Autor (CustomResource):
    pais = fields.CharField(attribute='pais')
    class Meta:
        queryset = Autor.objects.all()
        resource_name='autores'
        allowed_methods=['get','post','put']
        fields = ['id','nombre', 'apellido']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    
    def hydrate_pais(self, bundle):
        from countries.models import Country
        from tastypie import http
        country_name = bundle.data['pais']
        country = Country.objects.get(iso=country_name)
        if country:
            bundle.data['pais'] = country
            return bundle
        else:
            raise http.HttpNotFound('El pais con el codigo %s no existe'%country_name)
    
class Fotografia (CustomResource):
    class Meta:
        queryset = Fotografia.objects.all()
        resource_name='fotografias'
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
class Clasificacion (CustomResource):
    coleccion = fields.CharField(attribute='coleccion')
    categoria = fields.CharField(attribute='categoria')
    ficha = fields.CharField(attribute='ficha')
    
    class Meta:
        queryset = Clasificaciones.objects.all()
        resource_name='clasificacion'
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering={'coleccion':ALL, 'categoria':ALL}
        
    def hydrate_coleccion(self, bundle):
        from colecciones.models import Coleccion
        coleccion = bundle.data['coleccion']
        col = Coleccion.objects.get(nombre='coleccion')
        if col:
            bundle.data['coleccion'] = col
        else:
            raise http.HttpNotFound('no existe una coleccion con el nombre %s' % coleccion)
        return bundle
    
    def hydrate_categoria(self, bundle):
        from colecciones.models import Categoria
        categoria = bundle.data['categoria']
        cat = Categoria.objects.get(nombre='categoria')
        if cat:
            bundle.data['categoria'] = cat
        else:
            raise http.HttpNotFound('no existe una categoria con el nombre %s' % categoria)
        return bundle
    
    def hydrate_ficha(self, bundle):
        from registro.models import Ficha
        ficha = bundle.data['ficha']
        ficha_reg = Ficha.objects.get(nombre=ficha)
        if ficha_reg:
            bundle.data['ficha']= ficha_reg
        else:
            raise http.HttpNotFound('no existe una ficha con el nombre %s' % ficha)
        return bundle
    
enabled_resources=[Pieza,Autor, Fotografia, Clasificacion]
web_resources = [Exhibicion, Clasificacion]