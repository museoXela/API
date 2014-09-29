# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="t4r0"
__date__ ="$16-oct-2013 18:46:32$"

from django.contrib import admin
from usuarios.models import Perfil, Publicacion

admin.site.register([Perfil, Publicacion])