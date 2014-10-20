from django.conf.urls import patterns, include, url
from tastypie.api import Api
from django.contrib import admin
from bicefalo.utils import autodiscover
admin.autodiscover()
api = Api(api_name='v1')
def register_resources(resources=None):
    if not resources is None:
        for resource in resources:
            api.register(resource())
            
autodiscover('resources','enabled_resources', register_resources)
urlpatterns = patterns('',
    url(r'/admin/', include(admin.site.urls)),
    url(r'/oAuth/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^api/', include(api.urls)),
)
