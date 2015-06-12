# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0003_auto_20150607_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeFisica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cirurgia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observacao', models.CharField(max_length=50)),
                ('atividades_fisicas', models.ManyToManyField(to='teste.AtividadeFisica')),
                ('cirurgias', models.ManyToManyField(to='teste.Cirurgia')),
                ('doencas', models.ManyToManyField(related_name='historicodoenca', to='teste.Doenca')),
                ('historico_familiar_doencas', models.ManyToManyField(related_name='historicodoencafamiliar', to='teste.Doenca')),
            ],
        ),
        migrations.RemoveField(
            model_name='telefoneavaliador',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='telefonecliente',
            name='pessoa',
        ),
        migrations.DeleteModel(
            name='Avaliador',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='TelefoneAvaliador',
        ),
        migrations.DeleteModel(
            name='TelefoneCliente',
        ),
    ]
