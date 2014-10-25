# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='hora',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
    ]
