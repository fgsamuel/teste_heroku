# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_auto_20150614_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 6, 14, 19, 20, 57, 306342, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dadosvitais',
            name='pa_diastole',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dadosvitais',
            name='pa_sistole',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
