#!/usr/bin/python
# -*- coding: utf-8 -*-
from bicefalo.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from models import Categoria, Coleccion

class Categoria(ModelResource):
    class Meta:
        queryset = Categoria.objects.all()
        resource_name='categorias'
        allowed_methods = ['get','post' ,'put']
        fields = ['nombre']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"] 
    
class Coleccion(ModelResource):
    class Meta:
        queryset = Coleccion.objects.all()
        resource_name='colecciones'
        allowed_methods = ['get', 'post', 'put']
        fields = ['nombre']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()  
         
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]     

