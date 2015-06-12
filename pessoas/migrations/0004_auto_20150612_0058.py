# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0003_auto_20150610_0140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliador',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nome']},
        ),
    ]
