# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliador',
            name='data_nascimento',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(null=True, blank=True),
        ),
    ]
