# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '__first__'),
        ('piezas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50, null=True, blank=True)),
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
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
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
            name='Traslado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True, null=True)),
                ('bodega', models.BooleanField(default=True)),
                ('caja', models.ForeignKey(to='traslados.Caja')),
                ('codigoPieza', models.ForeignKey(to='piezas.Pieza')),
                ('responsable', models.ForeignKey(to='usuarios.Perfil')),
            ],
            options={
                'db_table': 'Traslado',
                'verbose_name': 'traslado',
                'verbose_name_plural': 'traslados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vitrina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.TextField(null=True, blank=True)),
                ('sala', models.ForeignKey(to='traslados.Sala')),
            ],
            options={
                'db_table': 'Vitrina',
                'verbose_name': 'vitrina',
                'verbose_name_plural': 'vitrinas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='traslado',
            name='vitrina',
            field=models.ForeignKey(to='traslados.Vitrina'),
            preserve_default=True,
        ),
    ]
