# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0001_initial'),
        ('piezas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campoEstructura', models.IntegerField()),
                ('tipoCampo', models.SmallIntegerField()),
                ('valorTexto', models.CharField(max_length=50, null=True, blank=True)),
                ('valorTextoLargo', models.TextField(null=True, blank=True)),
                ('valorFecha', models.DateField(null=True, blank=True)),
                ('valorNumerico', models.FloatField(null=True, blank=True)),
                ('valorRadio', models.SmallIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'Campo',
                'verbose_name': 'campo de registro',
                'verbose_name_plural': 'campos de registro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
                ('estructura', jsonfield.fields.JSONField(default=__builtin__.dict)),
                ('consolidacion', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Ficha',
                'verbose_name': 'ficha de registro',
                'verbose_name_plural': 'fichas de registro',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True)),
                ('consolidacion', models.BooleanField(default=False)),
                ('registroConsolidacion', models.ForeignKey(related_name=b'registro', blank=True, to='operaciones.Consolidacion')),
                ('registroPieza', models.ForeignKey(related_name=b'registro', blank=True, to='piezas.Pieza')),
            ],
            options={
                'db_table': 'Registro',
                'verbose_name': 'registro de pieza',
                'verbose_name_plural': 'registro de piezas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ValorCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=45)),
                ('seleccionado', models.BooleanField(default=False)),
                ('campo', models.ForeignKey(related_name=b'valorCheck', to='registro.Campo')),
            ],
            options={
                'db_table': 'ValorCheck',
                'verbose_name': 'campo de valor m\xfaltiple',
                'verbose_name_plural': 'campos de valor m\xfaltiple',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campo',
            name='registro',
            field=models.ForeignKey(related_name=b'detalle', to='registro.Registro'),
            preserve_default=True,
        ),
    ]
