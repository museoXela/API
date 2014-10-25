#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from django.contrib.auth.models import User

class UserResource(CustomResource):    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'usuarios'
        fields = ['username','date_joined','first_name','last_name','is_staff']       
        detail_uri_name = 'username'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    
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
        
enabled_resources=[UserResource]