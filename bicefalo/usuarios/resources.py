#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from django.contrib.auth.models import User,Group
from models import Perfil
from tastypie import fields

class Groups(CustomResource):
    class Meta:
        queryset = Group.objects.all()
        resource_name='grupos'
        allowed_methods=['get']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    
class UserResource(CustomResource):
    fotografia = fields.CharField(null = True)
    biografia = fields.CharField(null = True)
    pais = fields.CharField(null=True)
    filiacion = fields.CharField(null = True)
    voluntario = fields.BooleanField(null = True)
    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'usuarios'
        fields = ['username','date_joined','first_name','last_name','is_staff']       
        detail_uri_name = 'username'
        allowed_methods=['get','post','put','patch']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    
    def hydrate_fotografia(self, bundle):
        if 'fotografia' in bundle.data:
            bundle.obj.perfil.fotografia = bundle.data['fotografia']
        return bundle
    
    def dehydrate_fotografia(self, bundle):
        return unicode(bundle.obj.perfil.fotografia)
    
    def hydrate_filiacion(self, bundle):
        if 'filiacion' in bundle.data:
            bundle.obj.perfil.filiacionAcademica = bundle.data['filiacion']
        return bundle
    
    def dehydrate_filiacion(self, bundle):
        return bundle.obj.perfil.filiacionAcademica
    
    def hydrate_pais(self, bundle):
        from countries.models import Country
        from tastypie import http
        if 'pais' in bundle.data:
            try:
                pais = Country.objects.get(iso=bundle.data['pais'])
                bundle.obj.perfil.pais = pais
            except :
                raise http.HttpNotFound('No existe un pais con el iso %s' % bundle.data['pais'])
        return bundle
    
    def dehydrate_pais(self, bundle):
        return unicode(bundle.obj.perfil.pais)
    
    def hydrate_biografia(self, bundle):
        if 'biografia' in bundle.data:
            bundle.obj.perfil.biografia = bundle.data['biografia']
        return bundle
    
    def dehydrate_biografia(self, bundle):
        return unicode(bundle.obj.perfil.biografia)
    
    def hydrate_voluntario(self, bundle):
        if 'voluntario' in bundle.data:
            bundle.obj.perfil.voluntario = bundle.data['voluntario']
        return bundle
    
    def dehydrate_voluntario(self, bundle):
        return bundle.obj.perfil.voluntario
    
    def login(self, request, **kwargs):
        from django.contrib.auth import authenticate, login      
        if request.method=='POST':
            data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                if user.is_active:
                    login(request,user)
                    bundle = self.build_bundle(obj=user, request=request)
                    bundle = self.full_dehydrate(bundle)                    
                    return self.create_response(request,bundle)
                else:
                    return self.create_response(request,{'error':'tu cuenta está deshabilitada'},response_class=HttpForbidden)
            else:
                return self.create_response(request,{'error':'revisa tus datos y vuelve a intentarlo'},
                                            response_class=HttpBadRequest)
        else:
            return self.create_response(request,{'error':'solo se admite el método POST'}, response_class=HttpMethodNotAllowed)
    
    def logout(self,request, **kwargs):
        from django.contrib.auth import logout
        if request.method=='POST':
            logout(request)
        else:
            return self.create_response(request,{'error':'solo se admite el método POST'}, response_class=HttpMethodNotAllowed)
        return self.create_response(request,{'mensaje':'Has salido del sistema'})
    
    def prepend_urls(self):
        from django.conf.urls import url
        return [
            url(r'^usuarios/(?P<username>\w+)/$', self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
            url(r'^login/$', self.wrap_view('login'), name='login'),
            url(r'^logout/$', self.wrap_view('logout'), name='logout'),
            ]
class Voluntario(CustomResource):
    username=fields.CharField(readonly=True, attribute='usuario')
    nombre=fields.CharField(null=True)
    apellido=fields.CharField(null=True)
    investigaciones = fields.ListField(null=True)
    class Meta:
        queryset = Perfil.objects.filter(voluntario=True)
        resource_name='voluntarios'
        allowed_methods=['get']
        fields=['id','biografia', 'fotografia']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    
    def dehydrate_nombre(self, bundle):
        return unicode(bundle.obj.usuario.first_name)
    
    def dehydrate_apellido(self, bundle):
        return unicode(bundle.obj.usuario.last_name)    
    
    def dehydrate_investigaciones(self, bundle):
        return self.get_investigaciones(bundle.obj, bundle.request)
        
    def get_investigaciones(self, obj, request):
        from investigacion.resources import CustomInvestigacion
        list = obj.investigaciones.order_by('-fecha')[:3]
        objects = []
        res = CustomInvestigacion()
        for investigacion in list:
            bundle = res.build_bundle(obj=investigacion, request = request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)
        return objects
    
enabled_resources=[UserResource, Groups]
web_resources=[Voluntario]