from bicefalo.authentication import OAuth20Authentication
from django.contrib.auth.models import User
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie import fields

class UserResource(ModelResource):
    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        allowed_methods = ['get','post' ,'put', 'patch']
        fields = ['date_joined','first_name','last_name','is_staff', 'username']       
        detail_uri_name = 'username'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]
        
    