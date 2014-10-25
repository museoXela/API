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
    class Meta:
        queryset = User.objects.all()
        resource_name = 'usuarios'
        fields = ['username','date_joined','first_name','last_name','is_staff']       
        detail_uri_name = 'username'
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    
    def hydrate_fotografia(self, bundle):
        bundle.obj.perfil.fotografia = bundle.data['fotografia']
        bundle.obj.perfil.save()
        return bundle
        
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
    
    def dehydrate_investigaciones(self, request, bundle):
        return self.get_investigaciones(bundle.obj)
        
    def get_investigaciones(self, obj):
        from investigacion.resources import Investigacion
        from tastypie.utils import trailing_slash
        list = obj.investigaciones.order_by('-fecha')[:3]
        objects = []
        for investigacion in list:
            objects.append('/%s/investigaciones/%s%s' %(self.api_name, investigacion.pk, trailing_slash()))
        return objects
    
enabled_resources=[UserResource, Groups]
web_resources=[Voluntario]