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
                ('observacao', models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True)),
            ],
            options={
                'abstract': False,
            },
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
                ('descricao', models.CharField(max_length=100, verbose_name='Descri\xe7\xe3o')),
                ('observacao', models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True)),
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
                'verbose_name': 'Medica\xe7\xe3o',
                'verbose_name_plural': 'Medica\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Circunferencias',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('pescoco', models.IntegerField(null=True, verbose_name='Pesco\xe7o', blank=True)),
                ('ombros', models.IntegerField(null=True, blank=True)),
                ('torax_relaxado', models.IntegerField(null=True, verbose_name='T\xf3rax relaxado', blank=True)),
                ('torax_contraido', models.IntegerField(null=True, verbose_name='T\xf3rax contra\xeddo', blank=True)),
                ('biceps_direito_relaxado', models.IntegerField(null=True, verbose_name='B\xedceps direito relaxado', blank=True)),
                ('biceps_direito_contraido', models.IntegerField(null=True, verbose_name='B\xedceps direito contra\xeddo', blank=True)),
                ('biceps_esquerdo_relaxado', models.IntegerField(null=True, verbose_name='B\xedceps esquerdo relaxado', blank=True)),
                ('biceps_esquerdo_contraido', models.IntegerField(null=True, verbose_name='B\xedceps esquerdo contra\xeddo', blank=True)),
                ('cintura', models.IntegerField(null=True, blank=True)),
                ('abdomen', models.IntegerField(null=True, blank=True)),
                ('quadril', models.IntegerField(null=True, blank=True)),
                ('coxa_direita', models.IntegerField(null=True, blank=True)),
                ('coxa_esquerda', models.IntegerField(null=True, blank=True)),
                ('panturrilha_direita', models.IntegerField(null=True, blank=True)),
                ('panturrilha_esquerda', models.IntegerField(null=True, blank=True)),
                ('observacao', models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DadosVitais',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('frequencia_cardiaca', models.IntegerField(null=True, verbose_name='Frequ\xeancia card\xedaca', blank=True)),
                ('pa_sistole', models.IntegerField(null=True, verbose_name='Press\xe3o Arterial - Sistole', blank=True)),
                ('pa_diastole', models.IntegerField(null=True, verbose_name='Press\xe3o Arterial - Diastole', blank=True)),
                ('observacao', models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormularioPARQ',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('p1', models.NullBooleanField(default=False, verbose_name=b'1 - Seu m\xc3\xa9dico j\xc3\xa1 disse que voc\xc3\xaa possui um problema card\xc3\xadaco e recomendou atividades f\xc3\xadsicas apenas sob supervis\xc3\xa3o m\xc3\xa9dica?')),
                ('p2', models.NullBooleanField(default=False, verbose_name=b'2 - Voc\xc3\xaa tem dor no peito provocada por atividades f\xc3\xadsicas?')),
                ('p3', models.NullBooleanField(default=False, verbose_name=b'3 - Voc\xc3\xaa sentiu dor no peito no \xc3\xbaltimo m\xc3\xaas?')),
                ('p4', models.NullBooleanField(default=False, verbose_name=b'4 - Voc\xc3\xaa j\xc3\xa1 perdeu a consci\xc3\xaancia em alguma ocasi\xc3\xa3o ou sofreu alguma queda em virtude de tontura?')),
                ('p5', models.NullBooleanField(default=False, verbose_name=b'5 - Voc\xc3\xaa tem algum problema \xc3\xb3sseo ou articular que poderia agravar-se com a pr\xc3\xa1tica de atividades f\xc3\xadsicas?')),
                ('p6', models.NullBooleanField(default=False, verbose_name=b'6 - Algum m\xc3\xa9dico j\xc3\xa1 lhe prescreveu medicamento para press\xc3\xa3o arterial ou para o cora\xc3\xa7\xc3\xa3o? ')),
                ('p7', models.NullBooleanField(default=False, verbose_name=b'7 - Voc\xc3\xaa tem conhecimento, por informa\xc3\xa7\xc3\xa3o m\xc3\xa9dica ou pela pr\xc3\xb3pria experi\xc3\xaancia, de algum motivo que poderia imped\xc3\xad-lo de participar de atividades fisicas sem supervis\xc3\xa3o m\xc3\xa9dica? ')),
                ('observacao', models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('observacao', models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True)),
                ('atividades_fisicas', models.ManyToManyField(to='avaliacoes.AtividadeFisica', verbose_name='Atividades F\xedsicas', blank=True)),
                ('cirurgias', models.ManyToManyField(to='avaliacoes.Cirurgia', blank=True)),
                ('doencas', models.ManyToManyField(related_name='historicodoenca', verbose_name='Doen\xe7as', to='avaliacoes.Doenca', blank=True)),
                ('historico_familiar_doencas', models.ManyToManyField(related_name='historicodoencafamiliar', verbose_name='Hist\xf3rico familiar de doen\xe7as', to='avaliacoes.Doenca', blank=True)),
                ('medicacoes', models.ManyToManyField(to='avaliacoes.Medicacao', verbose_name='Medica\xe7\xf5es', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Objetivos',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('hipertrofia', models.BooleanField()),
                ('condicionamento_fisico', models.BooleanField(verbose_name='Condicionamento F\xedsico')),
                ('diminuicao_percentual_gordura', models.BooleanField(verbose_name='Redu\xe7\xe3o do percentual de Gordura')),
                ('melhorar_postura', models.BooleanField()),
                ('enrijecimento', models.BooleanField()),
                ('treino_forca', models.BooleanField(verbose_name='Treino de for\xe7a')),
                ('flexibilidade', models.BooleanField()),
                ('observacao', models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PesoAltura',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('peso', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('altura', models.IntegerField(null=True, blank=True)),
                ('observacao', models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plicometria',
            fields=[
                ('avaliacao', models.OneToOneField(primary_key=True, serialize=False, to='avaliacoes.Avaliacao')),
                ('subscapular', models.IntegerField(null=True, blank=True)),
                ('triceps_braquial', models.IntegerField(null=True, verbose_name='Tr\xedceps braquial', blank=True)),
                ('peitoral', models.IntegerField(null=True, blank=True)),
                ('axilar_media', models.IntegerField(null=True, verbose_name='Axiliar m\xe9dia', blank=True)),
                ('supra_iliaca', models.IntegerField(null=True, verbose_name='Supra il\xedaca', blank=True)),
                ('abdominal', models.IntegerField(null=True, blank=True)),
                ('coxa', models.IntegerField(null=True, blank=True)),
                ('panturrilha', models.IntegerField(null=True, blank=True)),
                ('biciptal', models.IntegerField(null=True, blank=True)),
                ('observacao', models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True)),
            ],
            options={
                'abstract': False,
            },
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
