# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20141025_1556'),
        ('piezas', '0002_auto_20141025_1556')
    ]

    operations = [
        migrations.CreateModel(
            name='Consolidacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('limpieza', models.BooleanField(default=False)),
                ('fechaInicio', models.DateField(auto_now=True, null=True)),
                ('fechaFin', models.DateField(null=True, blank=True)),
                ('codigoPieza', models.ForeignKey(to='piezas.Pieza')),
                ('responsable', models.ForeignKey(to='usuarios.Perfil')),
            ],
            options={
                'db_table': 'Consolidacion',
                'verbose_name': 'consolidacion',
                'verbose_name_plural': 'consolidaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('procedimiento', models.IntegerField(null=True, blank=True)),
                ('metodoMaterial', models.CharField(max_length=200, null=True, blank=True)),
                ('fecha', models.DateField(auto_now=True, null=True)),
                ('consolidacion', models.ForeignKey(to='operaciones.Consolidacion')),
            ],
            options={
                'db_table': 'Mantenimiento',
                'verbose_name': 'mantenimiento',
                'verbose_name_plural': 'mantenimientos',
            },
            bases=(models.Model,),
        ),
    ]
