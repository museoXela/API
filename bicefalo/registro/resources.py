from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from models import Ficha

class Ficha(CustomResource):
    estructura = fields.DictField(attribute='estructura')
    class Meta:
        queryset = Ficha.objects.all()
        resource_name='fichas'
        fields=['nombre','consolidacion']
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

enabled_resources=[Ficha]