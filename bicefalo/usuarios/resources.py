#!/usr/bin/python
# -*- coding: utf-8 -*-
from bicefalo.authentication import OAuth20Authentication
from django.contrib.auth.models import User
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie.http import *

class UserResource(ModelResource):
    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'usuarios'
        allowed_methods = ['get','post' ,'put']
        fields = ['username','date_joined','first_name','last_name','is_staff']       
        detail_uri_name = 'username'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
    
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
                    print(request.user)
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
        
    