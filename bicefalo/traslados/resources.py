#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ALL
from tastypie import fields
from models import Traslado, Caja as Cajas, Sala as  Salas, Vitrina as Vitrinas

class Traslado(CustomResource):
    responsable = fields.CharField(attribute='responsable')
    caja = fields.IntegerField(attribute='caja_id', null=True, blank=True)
    pieza = fields.CharField(attribute='pieza')
    vitrina = fields.IntegerField(attribute='vitrina_id', null=True, blank=True)

    class Meta:
        queryset= Traslado.objects.all()
        resource_name= 'traslados'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering = {'pieza':ALL, 'caja':ALL, 'vitrina':ALL, 'responsable':ALL}
        
    def hydrate_pieza(self, bundle):
        from piezas.models import Pieza
        pieza = bundle.data['pieza']
        if pieza:
            pieza = Pieza.objects.get(codigo=pieza)
            bundle.data['pieza'] = pieza
        return bundle
    
    def hydrate_responsable(self, bundle):
        from django.contrib.auth.models import User
        from usuarios.models import Perfil
        usuario = bundle.data['responsable']
        if usuario:
            usuario = User.objects.get(username=usuario).perfil
            bundle.data['responsable'] = usuario
        return bundle

    def hydrate_caja(self, bundle):
        from tastypie import http
        caja = bundle.data['caja']
        if caja:
            caja = Cajas.objects.get(id=caja)
            if caja:
                bundle.data['caja']=caja
                return bundle
            else:
                raise http.HttpBadRequest('Traslado debe degfinir una caja o una vitrina')
        return bundle

    def hydrate_vitrina(self, bundle):
        from tastypie import http
        from django.db.models import exceptions
        vitrina = bundle.data['vitrina']
        if vitrina:
            try:
                vitrina = Vitrinas.objects.get(id=vitrina)
                if vitrina:
                    bundle.data['vitrina']=vitrina
                    return bundle
                else:
                    raise http.HttpBadRequest('Traslado debe degfinir una caja o una vitrina')
            except exceptions.ObjectDoesNotExist:
                raise http.HttpNotFound('no existe una vitrina con ese número de registro')
        return bundle


class Caja(CustomResource):
    class Meta:
        queryset= Cajas.objects.all()
        resource_name= 'cajas'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering = {'codigo':ALL,}

class Sala(CustomResource):
    class Meta:
        queryset= Salas.objects.all()
        resource_name= 'salas'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering = {'nombre':ALL,'id':ALL}

class Vitrina(CustomResource):
    sala = fields.IntegerField(attribute='sala_id')
    class Meta:
        queryset= Vitrinas.objects.all()
        resource_name= 'vitrina'
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering = {'numero':ALL, 'sala':ALL,}

enabled_resources=[Traslado,Caja, Sala, Vitrina]
