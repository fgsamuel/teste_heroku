# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0003_auto_20150701_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagempostural',
            name='avaliacao',
            field=models.ForeignKey(related_name='fotos', default=11, to='avaliacoes.Avaliacao'),
            preserve_default=False,
        ),
    ]
