# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telefoneavaliador',
            old_name='pessoa',
            new_name='avaliador',
        ),
        migrations.RenameField(
            model_name='telefonecliente',
            old_name='pessoa',
            new_name='cliente',
        ),
    ]
