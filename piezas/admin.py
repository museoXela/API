from django.contrib import admin
from models import Autor, Fotografia, Pieza, Clasificacion

admin.site.register([Autor, Fotografia, Pieza, Clasificacion])