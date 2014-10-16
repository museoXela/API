from django.conf.urls import patterns, include, url
from tastypie.api import Api
from django.contrib import admin

# imports for api resources
from eventos.resources import Eventos
from investigacion.resources import Investigacion
from colecciones.resources import Coleccion, Categoria
from registro.resources import Ficha
from usuarios.resources import UserResource
from traslados.resources import Sala

resources = [UserResource(), Coleccion(), Categoria(), Investigacion(), Ficha(), Eventos(), Sala()]
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
