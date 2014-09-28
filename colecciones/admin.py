from django.contrib import admin
from models import Categoria, Clasificacion, Coleccion 

admin.site.register(Categoria, Coleccion, Clasificacion)
