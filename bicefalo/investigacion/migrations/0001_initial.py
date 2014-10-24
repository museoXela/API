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
            name='Investigacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=45)),
                ('contenido', models.TextField()),
                ('resumen', models.CharField(max_length=140, blank=True)),
                ('fecha', models.DateField(auto_now=True)),
                ('publicado', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(related_name=b'investigaciones', to='piezas.Autor')),
                ('editor', models.ForeignKey(to='usuarios.Perfil')),
                ('piezas', models.ManyToManyField(related_name=b'investigaciones', to='piezas.Pieza')),
            ],
            options={
                'db_table': 'Investigacion',
                'verbose_name': 'Investigaci\xf3n',
                'verbose_name_plural': 'Investigaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkInvestigacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField()),
                ('investigacion', models.ForeignKey(related_name=b'links', to='investigacion.Investigacion')),
            ],
            options={
                'db_table': 'LinkInvestigacion',
                'verbose_name': 'link de investigaci\xf3n',
                'verbose_name_plural': 'links de investigaci\xf3n',
            },
            bases=(models.Model,),
        ),
    ]
