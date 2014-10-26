# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '__first__'),
        ('colecciones', '__first__'),
        ('countries', '__first__'),
        ('usuarios', '0003_auto_20141025_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('pais', models.ForeignKey(related_name=b'autores', to='countries.Country')),
            ],
            options={
                'db_table': 'Autor',
                'verbose_name': 'autor',
                'verbose_name_plural': 'autores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(unique=True, max_length=50)),
                ('categoria', models.ForeignKey(related_name=b'clasificaciones', to='colecciones.Categoria')),
                ('coleccion', models.ForeignKey(related_name=b'clasificaciones', to='colecciones.Coleccion')),
                ('ficha', models.ForeignKey(related_name=b'clasificaciones', to='registro.Ficha')),
            ],
            options={
                'db_table': 'Clasificacion',
                'verbose_name': 'clasificaci\xf3n',
                'verbose_name_plural': 'clasificaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.SmallIntegerField(blank=True)),
                ('ruta', models.ImageField(upload_to=b'piezas')),
                ('perfil', models.BooleanField(default=True)),
                ('mantenimiento', models.ForeignKey(related_name=b'fotografias', blank=True, to='operaciones.Mantenimiento', null=True)),
            ],
            options={
                'db_table': 'Fotografia',
                'verbose_name': 'fotograf\xeda',
                'verbose_name_plural': 'fotograf\xedas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('codigo', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('codigoSlug', models.SlugField(blank=True)),
                ('registroIDAEH', models.BooleanField(default=False)),
                ('codigoIDAEH', models.CharField(max_length=25, blank=True)),
                ('archivoIDAEH', models.FileField(null=True, upload_to=b'files', blank=True)),
                ('nombre', models.CharField(max_length=140, blank=True)),
                ('descripcion', models.TextField()),
                ('fechaIngreso', models.DateField(auto_now=True)),
                ('procedencia', models.CharField(max_length=50, blank=True)),
                ('regionCultural', models.SmallIntegerField(null=True, blank=True)),
                ('observaciones', models.TextField(blank=True)),
                ('maestra', models.BooleanField(default=False)),
                ('exhibicion', models.BooleanField(default=False)),
                ('altura', models.FloatField(null=True, blank=True)),
                ('ancho', models.FloatField(null=True, blank=True)),
                ('grosor', models.FloatField(null=True, blank=True)),
                ('largo', models.FloatField(null=True, blank=True)),
                ('diametro', models.FloatField(null=True, blank=True)),
                ('autor', models.ForeignKey(related_name=b'creaciones', blank=True, to='piezas.Autor', null=True)),
                ('clasificacion', models.ForeignKey(related_name=b'piezas', to='piezas.Clasificacion')),
                ('pais', models.ForeignKey(related_name=b'piezas', blank=True, to='countries.Country', null=True)),
                ('responsableRegistro', models.ForeignKey(related_name=b'piezas_registradas', to='usuarios.Perfil')),
            ],
            options={
                'db_table': 'Pieza',
                'verbose_name': 'pieza',
                'verbose_name_plural': 'piezas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fotografia',
            name='pieza',
            field=models.ForeignKey(blank=True, to='piezas.Pieza', null=True),
            preserve_default=True,
        ),
    ]
