from django.db import models
from usuarios.models import Perfil
from countries.models import Country
from colecciones.models import Clasificacion
from operaciones.models import Mantenimiento

class Autor(models.Model):
    pais = models.ForeignKey(Country, related_name='autores')
    nombre = models.CharField()
    apellido = models.CharField()
    
    def __unicode__(self):
        return self.nombre + ' ' + self.apellido
    
    
class Pieza(models.Model):
    prepopulated_fields = {'slug':('codigoSlug',)}
    
    #Definición de campos
    codigo = models.CharField(primary_key=True, max_length=20)
    codigoSlug = models.SlugField()
    clasificacion = models.ForeignKey(Clasificacion, related_name='piezas')
    autor = models.ForeignKey(Autor, blank=True, related_name='creaciones')
    responsableRegistro = models.ForeignKey(Perfil, related_name='piezas_registradas')
    registroIDAEH = models.BooleanField(default=False, blank=True)
    codigoIDAEH = models.CharField(max_length=25, blank=True, null=False)
    archivoIDAEH = models.FileField(blank=True, null=True, upload_to="files")
    nombre = models.CharField(max_length=140, blank=True)
    descripcion = models.TextField()
    fechaIngreso = models.DateField()
    procedencia = models.CharField(max_length=50, blank=True)
    pais = models.ForeignKey(Country, blank=True, null=True, related_name='piezas')
    regionCultural = models.SmallIntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True)
    maestra = models.BooleanField(default=False, blank=True)
    exhibicion = models.BooleanField(default=False, blank =True)
    altura = models.FloatField(blank=True, null=True)
    ancho = models.FloatField(blank=True)
    grosor = models.FloatField(blank=True)
    largo = models.FloatField(blank=True)
    diametro = models.FloatField(blank=True)
    
    def __unicode__(self):
        return self.codigo

class Fotografia(models.Model):
    mantenimiento = models.ForeignKey(Mantenimiento, blank=True, null=True)
    pieza = models.ForeignKey(Pieza, blank=True, null=True)
    tipo = models.SmallIntegerField(blank=True)
    ruta = models.ImageField(upload_to='piezas')
    perfil = models.BooleanField(default=True)
    
    