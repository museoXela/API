from django.contrib import admin
from models import Autor, Fotografia, Pieza

admin.site.register(Autor, Fotografia, Pieza)