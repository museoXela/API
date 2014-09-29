#!/usr/bin/python
# -*- coding: utf-8 -*-
from bicefalo.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from models import Investigacion

class Investigacion(ModelResource):
    class Meta:
        queryset= Investigacion.objects.all()
        resource_name='investigaciones'
        allowed_methods = ['get','post' ,'put']
        fields = ['titulo', 'contenido', 'resumen', 'autor', 'fecha', 'editor']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"] 