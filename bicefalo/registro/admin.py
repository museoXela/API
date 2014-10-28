from django.contrib import admin
from django import forms
from jsonfield.widgets import JSONWidget
from models import Campo, Ficha, Registro, ValorCheck
class CampoInLine(admin.TabularInline):
    model = Campo
    extra = 1
class ValorCheckInline(admin.TabularInline):
    model = ValorCheck
    extra = 1
    
class FeedAdmin(admin.ModelAdmin):
    inlines = (CampoInLine,)
    
class FichaForm(forms.ModelForm):
    class Meta:
        model=Ficha
        widgets = {'estructura':JSONWidget(),}
        fields = ['nombre','estructura', 'consolidacion']
        
class FichaAdmin(admin.ModelAdmin):
    form = FichaForm

admin.site.register(Ficha, FichaAdmin)
admin.site.register( Registro,FeedAdmin)