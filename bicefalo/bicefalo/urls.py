from django.conf.urls import patterns, include, url
from tastypie.api import Api
from django.contrib import admin
from usuarios.resources import UserResource
from colecciones.resources import Coleccion, Categoria
from investigacion.resources import Investigacion

resources = [UserResource(), Coleccion(), Categoria(), Investigacion()]
admin.autodiscover()
api = Api(api_name='v1')
for resource in resources:
    api.register(resource)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bicefalo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(api.urls)),
)
