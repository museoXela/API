from __future__ import unicode_literals
from bicefalo.utils import CustomResource
from models import Pieza, Autor, Fotografia, Clasificacion


# Create your views here.

class Pieza (CustomResource):
    class Meta:
        queryset = Pieza.objects.all()
        resource_name='piezas'

class Autor (CustomResource):
    class Meta:
        queryset = Autor.objects.all()
        resource_name='autores'
    
class Fotografia (CustomResource):
    class Meta:
        queryset = Fotografia.objects.all()
        resource_name='fotografias'
        
class Clasificacion (CustomResource):
    class Meta:
        queryset = Clasificacion.objects.all()
        resource_name='clasificacion'
        
enabled_resources=[Pieza,Autor, Fotografia, Clasificacion]