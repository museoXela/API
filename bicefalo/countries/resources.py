from __future__ import unicode_literals
from bicefalo.utils import CustomResource
from models import Country

class Pais(CustomResource):
    class Meta:
        queryset= Country.objects.all()
        resource_name='paises'
enabled_resources=[Pais]