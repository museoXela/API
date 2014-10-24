# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'db_table': 'Categoria',
                'verbose_name': 'categor\xeda',
                'verbose_name_plural': 'categor\xedas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'db_table': 'Coleccion',
                'verbose_name': 'Colecci\xf3n',
                'verbose_name_plural': 'Colecciones',
            },
            bases=(models.Model,),
        ),
    ]
