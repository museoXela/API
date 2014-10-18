from __future__ import unicode_literals
from bicefalo.utils import CustomResource
from tastypie import fields
from models import Ficha

class Ficha(CustomResource):
    estructura = fields.DictField(attribute='estructura')
    class Meta:
        queryset = Ficha.objects.all()
        resource_name='fichas'
        fields=['nombre','consolidacion']

enabled_resources=[Ficha]