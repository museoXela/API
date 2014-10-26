# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piezas', '0002_auto_20141025_1556'),
        ('usuarios', '0003_auto_20141025_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50, unique=True, null=True, blank=True)),
            ],
            options={
                'db_table': 'Caja',
                'verbose_name': 'caja',
                'verbose_name_plural': 'cajas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, unique=True, null=True, blank=True)),
                ('descripcion', models.TextField(max_length=50, null=True, blank=True)),
                ('fotografia', models.ImageField(default=b'salas/room.jpg', null=True, upload_to=b'salas', blank=True)),
            ],
            options={
                'db_table': 'Sala',
                'verbose_name': 'sala',
                'verbose_name_plural': 'salas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vitrina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=20, null=True, blank=True)),
                ('sala', models.ForeignKey(to='traslados.Sala')),
            ],
            options={
                'db_table': 'Vitrina',
                'verbose_name': 'vitrina',
                'verbose_name_plural': 'vitrinas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Traslado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True, null=True)),
                ('bodega', models.BooleanField(default=True)),
                ('caja', models.ForeignKey(blank=True, to='traslados.Caja', null=True)),
                ('pieza', models.ForeignKey(to='piezas.Pieza')),
                ('responsable', models.ForeignKey(to='usuarios.Perfil')),
                ('vitrina', models.ForeignKey(blank=True, to='traslados.Vitrina', null=True))
            ],
            options={
                'db_table': 'Traslado',
                'verbose_name': 'traslado',
                'verbose_name_plural': 'traslados',
            },
            bases=(models.Model,),
        ),
    ]
