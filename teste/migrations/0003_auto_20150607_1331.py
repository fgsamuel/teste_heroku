# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0002_auto_20150606_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefoneavaliador',
            name='avaliador',
        ),
        migrations.RemoveField(
            model_name='telefonecliente',
            name='cliente',
        ),
        migrations.AddField(
            model_name='telefoneavaliador',
            name='pessoa',
            field=models.ForeignKey(related_name='telefones', default=1, to='teste.Avaliador'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telefonecliente',
            name='pessoa',
            field=models.ForeignKey(related_name='telefones', default=1, to='teste.Cliente'),
            preserve_default=False,
        ),
    ]
