# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import avaliacoes.models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeFisica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Atividade F\xedsica',
                'verbose_name_plural': 'Atividades F\xedsicas',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
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
                'ordering': ['nome'],
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
                'verbose_name': 'Doen\xe7a',
                'verbose_name_plural': 'Doen\xe7as',
            },
        ),
        migrations.CreateModel(
            name='ImagemPostural',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(upload_to=avaliacoes.models.get_file_name)),
                ('descricao', models.CharField(max_length=100)),
                ('observacao', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Medica\xe7\xe3o',
                'verbose_name_plural': 'Medica\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Plicometria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscapular', models.IntegerField(null=True, blank=True)),
                ('triceps_braquial', models.IntegerField(null=True, blank=True)),
                ('peitoral', models.IntegerField(null=True, blank=True)),
                ('axilar_media', models.IntegerField(null=True, blank=True)),
                ('supra_iliaca', models.IntegerField(null=True, blank=True)),
                ('abdominal', models.IntegerField(null=True, blank=True)),
                ('coxa', models.IntegerField(null=True, blank=True)),
                ('panturrilha', models.IntegerField(null=True, blank=True)),
                ('biciptal', models.IntegerField(null=True, blank=True)),
                ('observacao', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Circunferencias',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
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
                ('observacao', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DadosVitais',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('frequencia_cardiaca', models.IntegerField(null=True, blank=True)),
                ('pa_sistole', models.IntegerField(null=True, blank=True)),
                ('pa_diastole', models.IntegerField(null=True, blank=True)),
                ('observacao', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormularioPARQ',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('p1', models.NullBooleanField(default=False)),
                ('p2', models.NullBooleanField(default=False)),
                ('p3', models.NullBooleanField(default=False)),
                ('p4', models.NullBooleanField(default=False)),
                ('p5', models.NullBooleanField(default=False)),
                ('p6', models.NullBooleanField(default=False)),
                ('p7', models.NullBooleanField(default=False)),
                ('observacao', models.CharField(max_length=300, blank=True)),
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
                ('medicacoes', models.ManyToManyField(to='avaliacoes.Medicacao', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Objetivos',
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
            name='PesoAltura',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('peso', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('altura', models.IntegerField(null=True, blank=True)),
                ('observacao', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='imagempostural',
            name='avaliacao',
            field=models.ForeignKey(related_name='fotos', to='avaliacoes.Avaliacao'),
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
