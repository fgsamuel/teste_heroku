# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 6, 14, 19, 19, 41, 485759, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dadosvitais',
            name='frequencia_cardiaca',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
