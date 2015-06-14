# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0003_auto_20150614_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Antropometria',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('observacao', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='historico',
            name='medicacoes',
            field=models.ManyToManyField(to='avaliacoes.Medicacao', blank=True),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='data',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Circunferencias',
            fields=[
                ('antropometria', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Antropometria')),
                ('pescoco', models.IntegerField(null=True, blank=True)),
                ('ombros', models.IntegerField(null=True, blank=True)),
                ('torax_relaxado', models.IntegerField(null=True, blank=True)),
                ('torax_contraido', models.IntegerField(null=True, blank=True)),
                ('biceps_direito_relaxado', models.IntegerField(null=True, blank=True)),
                ('biceps_direito_contraido', models.IntegerField(null=True, blank=True)),
                ('biceps_esquerdo_relaxado', models.IntegerField(null=True, blank=True)),
                ('biceps_esquerdo_contraido', models.IntegerField(null=True, blank=True)),
                ('cintura', models.IntegerField(null=True, blank=True)),
                ('abdomen', models.IntegerField(null=True, blank=True)),
                ('quadril', models.IntegerField(null=True, blank=True)),
                ('coxa_direita', models.IntegerField(null=True, blank=True)),
                ('coxa_esquerda', models.IntegerField(null=True, blank=True)),
                ('panturrilha_direita', models.IntegerField(null=True, blank=True)),
                ('panturrilha_esquerda', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PesoAltura',
            fields=[
                ('antropometria', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Antropometria')),
                ('peso', models.DecimalField(max_digits=5, decimal_places=2)),
                ('altura', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
