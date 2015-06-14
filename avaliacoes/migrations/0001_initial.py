# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeFisica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField(default=datetime.datetime(2015, 6, 14, 19, 13, 57, 695236, tzinfo=utc))),
                ('observacao', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cirurgia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medicacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Anamnese',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('hipertrofia', models.BooleanField()),
                ('condicionamento_fisico', models.BooleanField()),
                ('diminuicao_percentual_gordura', models.BooleanField()),
                ('melhorar_postura', models.BooleanField()),
                ('enrijecimento', models.BooleanField()),
                ('treino_forca', models.BooleanField()),
                ('flexibilidade', models.BooleanField()),
                ('observacao', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DadosVitais',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('frequencia_cardiaca', models.IntegerField(blank=True)),
                ('pa_sistole', models.IntegerField(blank=True)),
                ('pa_diastole', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormularioPARQ',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('p1', models.NullBooleanField()),
                ('p2', models.NullBooleanField()),
                ('p3', models.NullBooleanField()),
                ('p4', models.NullBooleanField()),
                ('p5', models.NullBooleanField()),
                ('p6', models.NullBooleanField()),
                ('p7', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('observacao', models.CharField(max_length=300, blank=True)),
                ('atividades_fisicas', models.ManyToManyField(to='avaliacoes.AtividadeFisica', blank=True)),
                ('cirurgias', models.ManyToManyField(to='avaliacoes.Cirurgia', blank=True)),
                ('doencas', models.ManyToManyField(related_name='historicodoenca', to='avaliacoes.Doenca', blank=True)),
                ('historico_familiar_doencas', models.ManyToManyField(related_name='historicodoencafamiliar', to='avaliacoes.Doenca', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='avaliador',
            field=models.ForeignKey(to='pessoas.Avaliador'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='cliente',
            field=models.ForeignKey(to='pessoas.Cliente'),
        ),
    ]
