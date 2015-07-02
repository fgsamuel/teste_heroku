# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import avaliacoes.models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_imagempostural'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagempostural',
            name='foto',
            field=models.ImageField(upload_to=avaliacoes.models.get_file_name),
        ),
    ]
