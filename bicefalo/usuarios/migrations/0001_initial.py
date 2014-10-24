# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('countries', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filiacionAcademica', models.CharField(max_length=50, blank=True)),
                ('fotografia', models.ImageField(default=b'users/default.png', null=True, upload_to=b'users', blank=True)),
                ('biografia', models.TextField(blank=True)),
                ('pais', models.ForeignKey(to='countries.Country', null=True)),
                ('usuario', models.OneToOneField(related_name=b'perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserDetail',
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True, null=True)),
                ('nombre', models.CharField(max_length=140)),
                ('publicacion', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('autor', models.ForeignKey(related_name=b'publicaciones', to='usuarios.Perfil')),
            ],
            options={
                'db_table': 'Publicacion',
                'verbose_name': 'publicaci\xf3n',
                'verbose_name_plural': 'publicaciones',
            },
            bases=(models.Model,),
        ),
    ]
