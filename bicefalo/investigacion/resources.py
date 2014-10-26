from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ObjectDoesNotExist, MultipleObjectsReturned
from tastypie.http import HttpGone, HttpMultipleChoices
from tastypie import fields
from tastypie.resources import ALL
from django.conf.urls import url
from models import Investigacion as Investigaciones, LinkInvestigacion

class LinkResource(CustomResource):
    class Meta:
        queryset = LinkInvestigacion.objects.all()
        resource_name = 'linksInvestigacion'
        fields = ['link']
        include_resource_uri = False
        

class Investigacion(CustomResource):
    links = fields.ListField(null = True)
    userFoto= fields.CharField(null=True, readonly=True)
    editor=fields.CharField(attribute='editor')
    class Meta:
        queryset= Investigaciones.objects.all()
        resource_name='investigaciones'
        fields = ['id','titulo', 'contenido', 'resumen', 'fecha']
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering={
                   'editor': ALL
                   }
        
    def get_links(self, request, obj):        
        res= LinkResource()
        list = obj.links.all()
        objects = []
        for comments in list:
            bundle = res.build_bundle(obj=comments, request=request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)
        return objects
    
    def dehydrate_userFoto(self, bundle):
        return unicode(bundle.obj.editor.fotografia)
    
    def dehydrate_links(self, bundle):
        return self.get_links(bundle.request, bundle.obj)
    
    def hydrate_editor(self, bundle):
        from django.contrib.auth.models import User
        from usuarios.models import Perfil
        usuario = bundle.data['editor']
        if usuario:
            usuario = User.objects.get(username=usuario).perfil
            bundle.data['editor'] = usuario
        return bundle
    
    def get_piezas(self, request, **kwargs):
        from piezas.resources import Exhibicion
        from tastypie.paginator import Paginator
        try:
            bundle = self.build_bundle(data={'pk':kwargs['pk']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this uri")
        res= Exhibicion()
        objects = []
        list = obj.piezas.all()
        list = Paginator(request.GET, list).page()['objects']
        for obj in list:
            bundle = res.build_bundle(obj=obj, request = request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)
        res.log_throttled_access(request)
        return res.create_response(request, objects)
    
    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\d+)/piezas/$" % self._meta.resource_name, self.wrap_view('get_piezas'), name="dispatch_piezas"),
        ]

class CustomInvestigacion(CustomResource):
    class Meta:
        queryset= Investigaciones.objects.all()
        resource_name='investigaciones'
        fields = ['id','titulo']
        allowed_methods=['get']
        include_resource_uri = False
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

enabled_resources=[Investigacion]
web_resources=[Investigacion]