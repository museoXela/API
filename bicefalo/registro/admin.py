from django.contrib import admin
from django import forms
from jsonfield.widgets import JSONWidget
from models import Campo, Ficha, Registro, ValorCheck

class FichaForm(forms.ModelForm):
    class Meta:
        model=Ficha
        widgets = {'estructura':JSONWidget(),}
        fields = ['nombre','estructura', 'consolidacion']
        
class FichaAdmin(admin.ModelAdmin):
    form = FichaForm

admin.site.register(Ficha, FichaAdmin)
admin.site.register([Campo, Registro, ValorCheck])