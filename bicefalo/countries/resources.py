from __future__ import unicode_literals
from bicefalo.authentication import OAuth20Authentication
from bicefalo.utils import CustomResource
from tastypie.authorization import DjangoAuthorization
from models import Country

class Pais(CustomResource):
    class Meta:
        queryset= Country.objects.all()
        resource_name='paises'
        allowed_methods=['get','post','put']
        always_return_data = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
enabled_resources=[Pais]