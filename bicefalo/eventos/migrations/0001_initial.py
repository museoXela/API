# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '__first__'),
        ('traslados', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=45, unique=True, null=True, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('afiche', models.ImageField(null=True, upload_to=b'afiches', blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('sala', models.ForeignKey(to='traslados.Sala')),
                ('usuario', models.ForeignKey(to='usuarios.Perfil')),
            ],
            options={
                'db_table': 'Eventos',
                'verbose_name': 'evento',
                'verbose_name_plural': 'eventos',
            },
            bases=(models.Model,),
        ),
    ]
