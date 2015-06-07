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
            name='cep',
            field=models.CharField(max_length=8, blank=True),
        ),
        migrations.AlterField(
            model_name='avaliador',
            name='complemento',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='avaliador',
            name='data_nascimento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='avaliador',
            name='email',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='avaliador',
            name='numero',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='avaliador',
            name='observacao',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=8, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='complemento',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observacao',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='telefoneavaliador',
            name='observacao',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='telefonecliente',
            name='observacao',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
