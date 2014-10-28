from django.contrib import admin
from piezas.models import Categoria, Coleccion, Clasificacion
class CategoriasInline(admin.TabularInline):
    model = Clasificacion
    extra = 1
    
class FeedAdmin(admin.ModelAdmin):
    inlines = (CategoriasInline,)
admin.site.register([Categoria,Coleccion], FeedAdmin)
