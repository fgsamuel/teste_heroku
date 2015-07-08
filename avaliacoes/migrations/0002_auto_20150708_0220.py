# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plicometria',
            name='id',
        ),
        migrations.AddField(
            model_name='plicometria',
            name='avaliacao',
            field=models.OneToOneField(primary_key=True, default=5, serialize=False, to='avaliacoes.Avaliacao'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='observacao',
            field=models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='circunferencias',
            name='biceps_direito_contraido',
            field=models.IntegerField(null=True, verbose_name='B\xedceps direito contra\xeddo', blank=True),
        ),
        migrations.AlterField(
            model_name='circunferencias',
            name='biceps_direito_relaxado',
            field=models.IntegerField(null=True, verbose_name='B\xedceps direito relaxado', blank=True),
        ),
        migrations.AlterField(
            model_name='circunferencias',
            name='biceps_esquerdo_contraido',
            field=models.IntegerField(null=True, verbose_name='B\xedceps esquerdo contra\xeddo', blank=True),
        ),
        migrations.AlterField(
            model_name='circunferencias',
            name='biceps_esquerdo_relaxado',
            field=models.IntegerField(null=True, verbose_name='B\xedceps esquerdo relaxado', blank=True),
        ),
        migrations.AlterField(
            model_name='circunferencias',
            name='observacao',
            field=models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='circunferencias',
            name='pescoco',
            field=models.IntegerField(null=True, verbose_name='Pesco\xe7o', blank=True),
        ),
        migrations.AlterField(
            model_name='circunferencias',
            name='torax_contraido',
            field=models.IntegerField(null=True, verbose_name='T\xf3rax contra\xeddo', blank=True),
        ),
        migrations.AlterField(
            model_name='circunferencias',
            name='torax_relaxado',
            field=models.IntegerField(null=True, verbose_name='T\xf3rax relaxado', blank=True),
        ),
        migrations.AlterField(
            model_name='dadosvitais',
            name='frequencia_cardiaca',
            field=models.IntegerField(null=True, verbose_name='Frequ\xeancia card\xedaca', blank=True),
        ),
        migrations.AlterField(
            model_name='dadosvitais',
            name='observacao',
            field=models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='dadosvitais',
            name='pa_diastole',
            field=models.IntegerField(null=True, verbose_name='Press\xe3o Arterial - Diastole', blank=True),
        ),
        migrations.AlterField(
            model_name='dadosvitais',
            name='pa_sistole',
            field=models.IntegerField(null=True, verbose_name='Press\xe3o Arterial - Sistole', blank=True),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='observacao',
            field=models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p1',
            field=models.NullBooleanField(default=False, verbose_name=b'1 - Seu m\xc3\xa9dico j\xc3\xa1 disse que voc\xc3\xaa possui um problema card\xc3\xadaco e recomendou atividades f\xc3\xadsicas apenas sob supervis\xc3\xa3o m\xc3\xa9dica?'),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p2',
            field=models.NullBooleanField(default=False, verbose_name=b'2 - Voc\xc3\xaa tem dor no peito provocada por atividades f\xc3\xadsicas?'),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p3',
            field=models.NullBooleanField(default=False, verbose_name=b'3 - Voc\xc3\xaa sentiu dor no peito no \xc3\xbaltimo m\xc3\xaas?'),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p4',
            field=models.NullBooleanField(default=False, verbose_name=b'4 - Voc\xc3\xaa j\xc3\xa1 perdeu a consci\xc3\xaancia em alguma ocasi\xc3\xa3o ou sofreu alguma queda em virtude de tontura?'),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p5',
            field=models.NullBooleanField(default=False, verbose_name=b'5 - Voc\xc3\xaa tem algum problema \xc3\xb3sseo ou articular que poderia agravar-se com a pr\xc3\xa1tica de atividades f\xc3\xadsicas?'),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p6',
            field=models.NullBooleanField(default=False, verbose_name=b'6 - Algum m\xc3\xa9dico j\xc3\xa1 lhe prescreveu medicamento para press\xc3\xa3o arterial ou para o cora\xc3\xa7\xc3\xa3o? '),
        ),
        migrations.AlterField(
            model_name='formularioparq',
            name='p7',
            field=models.NullBooleanField(default=False, verbose_name=b'7 - Voc\xc3\xaa tem conhecimento, por informa\xc3\xa7\xc3\xa3o m\xc3\xa9dica ou pela pr\xc3\xb3pria experi\xc3\xaancia, de algum motivo que poderia imped\xc3\xad-lo de participar de atividades fisicas sem supervis\xc3\xa3o m\xc3\xa9dica? '),
        ),
        migrations.AlterField(
            model_name='historico',
            name='atividades_fisicas',
            field=models.ManyToManyField(to='avaliacoes.AtividadeFisica', verbose_name='Atividades F\xedsicas', blank=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='doencas',
            field=models.ManyToManyField(related_name='historicodoenca', verbose_name='Doen\xe7as', to='avaliacoes.Doenca', blank=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='historico_familiar_doencas',
            field=models.ManyToManyField(related_name='historicodoencafamiliar', verbose_name='Hist\xf3rico familiar de doen\xe7as', to='avaliacoes.Doenca', blank=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='medicacoes',
            field=models.ManyToManyField(to='avaliacoes.Medicacao', verbose_name='Medica\xe7\xf5es', blank=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='observacao',
            field=models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='imagempostural',
            name='descricao',
            field=models.CharField(max_length=100, verbose_name='Descri\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='imagempostural',
            name='observacao',
            field=models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='objetivos',
            name='condicionamento_fisico',
            field=models.BooleanField(verbose_name='Condicionamento F\xedsico'),
        ),
        migrations.AlterField(
            model_name='objetivos',
            name='diminuicao_percentual_gordura',
            field=models.BooleanField(verbose_name='Redu\xe7\xe3o do percentual de Gordura'),
        ),
        migrations.AlterField(
            model_name='objetivos',
            name='observacao',
            field=models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='objetivos',
            name='treino_forca',
            field=models.BooleanField(verbose_name='Treino de for\xe7a'),
        ),
        migrations.AlterField(
            model_name='pesoaltura',
            name='observacao',
            field=models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='plicometria',
            name='axilar_media',
            field=models.IntegerField(null=True, verbose_name='Axiliar m\xe9dia', blank=True),
        ),
        migrations.AlterField(
            model_name='plicometria',
            name='observacao',
            field=models.CharField(max_length=300, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='plicometria',
            name='supra_iliaca',
            field=models.IntegerField(null=True, verbose_name='Supra il\xedaca', blank=True),
        ),
        migrations.AlterField(
            model_name='plicometria',
            name='triceps_braquial',
            field=models.IntegerField(null=True, verbose_name='Tr\xedceps braquial', blank=True),
        ),
    ]
