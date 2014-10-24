from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ObjectDoesNotExist, MultipleObjectsReturned
from tastypie.http import HttpGone, HttpMultipleChoices
from tastypie import fields
from tastypie.resources import ALL
from django.conf.urls import url
from models import Investigacion, LinkInvestigacion

class LinkResource(CustomResource):
    class Meta:
        queryset = LinkInvestigacion.objects.all()
        resource_name = 'linksInvestigacion'
        fields = ['link']
        include_resource_uri = False
        

class Investigacion(CustomResource):

    userFoto= fields.CharField(null=True, readonly=True)
    class Meta:
        queryset= Investigacion.objects.all()
        resource_name='investigaciones'
        fields = ['id','titulo', 'contenido', 'resumen', 'fecha', 'editor']
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        filtering={
                   'editor': ALL
                   }
        
    def get_links(self, request, **kwargs):
        try:
            bundle = self.build_bundle(data={'pk':kwargs['pk']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this uri")
        res= LinkResource()
        list = obj.links.all()
        objects = []
        for comments in list:
            bundle = res.build_bundle(obj=comments, request=request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)

        res.log_throttled_access(request)
        return res.create_response(request, objects)
    
    def dehydrate_userFoto(self, bundle):
        return unicode(bundle.obj.editor.fotografia)
    
    def get_piezas(self, request, **kwargs):
        from piezas.resources import Pieza
        try:
            bundle = self.build_bundle(data={'pk':kwargs['pk']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this uri")
        res= Pieza()
        list = obj.piezas.all()
        objects = []
        for comments in list:
            bundle = res.build_bundle(obj=comments, request=request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)

        res.log_throttled_access(request)
        return res.create_response(request, objects)
     
    def prepend_urls(self):
        return [
        url(r'^investigaciones/(?P<pk>\d+)/links/$', self.wrap_view('get_links'),name='investigacion_links'),]


enabled_resources=[Investigacion]
web_resources=[Investigacion]