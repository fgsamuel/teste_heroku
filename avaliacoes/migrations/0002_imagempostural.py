# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagemPostural',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.FileField(upload_to=b'imagens_posturais/clienteId')),
                ('descricao', models.CharField(max_length=100)),
                ('observacao', models.CharField(max_length=300, blank=True)),
            ],
        ),
    ]
