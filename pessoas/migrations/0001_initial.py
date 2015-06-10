# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField(blank=True)),
                ('email', models.CharField(max_length=150, blank=True)),
                ('cep', models.CharField(max_length=8, blank=True)),
                ('numero', models.CharField(max_length=10, blank=True)),
                ('complemento', models.CharField(max_length=50, blank=True)),
                ('observacao', models.CharField(max_length=300, blank=True)),
                ('login', models.CharField(max_length=15)),
                ('senha', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField(blank=True)),
                ('email', models.CharField(max_length=150, blank=True)),
                ('cep', models.CharField(max_length=8, blank=True)),
                ('numero', models.CharField(max_length=10, blank=True)),
                ('complemento', models.CharField(max_length=50, blank=True)),
                ('observacao', models.CharField(max_length=300, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TelefoneAvaliador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ddd', models.CharField(max_length=2)),
                ('numero', models.CharField(max_length=9)),
                ('observacao', models.CharField(max_length=300, blank=True)),
                ('pessoa', models.ForeignKey(related_name='telefones', to='pessoas.Avaliador')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TelefoneCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ddd', models.CharField(max_length=2)),
                ('numero', models.CharField(max_length=9)),
                ('observacao', models.CharField(max_length=300, blank=True)),
                ('pessoa', models.ForeignKey(related_name='telefones', to='pessoas.Cliente')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
