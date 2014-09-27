from django.conf.urls import patterns, include, url
from tastypie.api import Api
from django.contrib import admin
from usuarios.resources import UserResource
admin.autodiscover()
api = Api(api_name='v1')
api.register(UserResource())
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bicefalo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
)
