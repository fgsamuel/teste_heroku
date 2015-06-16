# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0004_auto_20150614_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioparq',
            name='p1',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p2',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p3',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p4',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p5',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p6',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p7',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pesoaltura',
            name='peso',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
    ]
