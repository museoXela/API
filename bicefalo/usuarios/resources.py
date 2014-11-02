#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from django.contrib.auth.models import User,Group
from tastypie.resources import ALL
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
    fotografia = fields.CharField(null=True)
    biografia = fields.CharField(null=True)
    pais = fields.CharField(null=True)
    filiacion = fields.CharField(null=True)
    voluntario = fields.BooleanField(null=True)
    fullName = fields.CharField(null=True, readonly=True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'usuarios'
        fields = ['username','date_joined','first_name','last_name','is_staff','email','is_active']       
        detail_uri_name = 'username'
        allowed_methods=['get','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering = {'username':ALL, 'is_active':ALL}
        
    def hydrate_fullName(self, bundle):
        return bundle.obj.first_name +  ' ' + bundle.obj.last_name
    def hydrate_fotografia(self, bundle):
        if 'fotografia' in bundle.data and bundle.obj.perfil:
            bundle.obj.perfil.fotografia = bundle.data['fotografia']
        return bundle
        
    def dehydrate_fotografia(self, bundle):
        return unicode(bundle.obj.perfil.fotografia)
    
    def hydrate_filiacion(self, bundle):
        if 'filiacion' in bundle.data and bundle.obj.perfil:
            bundle.obj.perfil.filiacionAcademica = bundle.data['filiacion']
        return bundle
    
    def dehydrate_filiacion(self, bundle):
        return bundle.obj.perfil.filiacionAcademica
    
    def hydrate_pais(self, bundle):
        from countries.models import Country
        from tastypie import http
        if 'pais' in bundle.data and bundle.obj.perfil:
            try:
                pais = Country.objects.get(iso=bundle.data['pais'])
                bundle.obj.perfil.pais = pais
            except :
                raise http.HttpNotFound('No existe un pais con el iso %s' % bundle.data['pais'])
        return bundle
    
    def dehydrate_pais(self, bundle):
        return unicode(bundle.obj.perfil.pais.iso)
    
    def hydrate_biografia(self, bundle):
        if 'biografia' in bundle.data and bundle.obj.perfil:
            bundle.obj.perfil.biografia = bundle.data['biografia']
        return bundle
    
    def dehydrate_biografia(self, bundle):
        return unicode(bundle.obj.perfil.biografia)
    
    def hydrate_voluntario(self, bundle):
        if 'voluntario' in bundle.data and bundle.obj.per:
            bundle.obj.perfil.voluntario = bundle.data['voluntario']
        return bundle
    
    def dehydrate_voluntario(self, bundle):
        return bundle.obj.perfil.voluntario
    
    def login(self, request, **kwargs):
        from django.contrib.auth import authenticate, login   
        from tastypie import http   
        if request.method=='POST':
            data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                if user.is_active:
                    login(request,user)
                    bundle = self.build_bundle(obj=user, request=request)
                    bundle = self.full_dehydrate(bundle)                    
                    return self.create_response(request,bundle, response_class=http.HttpCreated)
                else:
                    return self.create_response(request,{'error':'tu cuenta está deshabilitada'},response_class=http.HttpForbidden)
            else:
                return self.create_response(request,{'error':'revisa tus datos y vuelve a intentarlo'},
                                            response_class=http.HttpBadRequest)
        else:
            return self.create_response(request,{'error':'solo se admite el método POST'}, response_class=http.HttpMethodNotAllowed)
    
    def logout(self,request, **kwargs):
        from django.contrib.auth import logout
        from tastypie import http
        if request.method=='POST':
            logout(request)
        else:
            return self.create_response(request,{'error':'solo se admite el método POST'}, response_class=http.HttpMethodNotAllowed)
        return self.create_response(request,{'mensaje':'Has salido del sistema'})
        
    def create(self, request, **kwargs):
        from tastypie import http
        if request.method == 'POST':
            data = self.deserialize(request, request.body, format='application/json')
            User.objects.create_user(data['username'], data['email'], data['password'])
            return self.create_response(request,{'mensaje':'Usuario creado con éxito'}, response_class=http.HttpCreated)
        return self.create_response(request,{'error':'solo se admite el método POST'}, response_class=http.HttpMethodNotAllowed)
    
    def prepend_urls(self):
        from django.conf.urls import url
        return [
            url(r'^usuarios/(?P<username>\w+)/$', self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
            url(r'^login/$', self.wrap_view('login'), name='login'),
            url(r'^logout/$', self.wrap_view('logout'), name='logout'),
            url(r'^registrar/$', self.wrap_view('create'), name='create_user'),
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