# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_perfil_voluntario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fotografia',
            field=models.URLField(null=True, blank=True),
        ),
    ]
