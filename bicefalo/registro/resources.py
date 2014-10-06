#!/usr/bin/python
# -*- coding: utf-8 -*-
from bicefalo.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie import fields
from models import Ficha

class Ficha(ModelResource):
    estructura = fields.DictField(attribute='estructura')
    class Meta:
        queryset = Ficha.objects.all()
        resource_name='fichas'
        allowed_methods=['get', 'put', 'post']
        fields=['nombre','consolidacion']        
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()        
    
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"] 
        