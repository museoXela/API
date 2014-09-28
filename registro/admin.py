from django.contrib import admin
from models import Campo, Ficha, Registro, ValorCheck

admin.site.register(Campo, Ficha, Registro, ValorCheck)