# -*- coding: utf-8 -*-

from django.db import models
from pessoas.models import Avaliador, Cliente

class Avaliacao(models.Model):
	cliente = models.ForeignKey(Cliente)
	avaliador = models.ForeignKey(Avaliador)
	data = models.DateField()
	observacao = models.CharField(max_length=300, blank=True)


class Anamnese(models.Model):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	hipertrofia = models.BooleanField(blank=True)
	condicionamento_fisico = models.BooleanField(blank=True)
	diminuicao_percentual_gordura = models.BooleanField(blank=True)
	melhorar_postura = models.BooleanField(blank=True)
	enrijecimento = models.BooleanField(blank=True)
	treino_forca = models.BooleanField(blank=True)
	flexibilidade = models.BooleanField(blank=True)
	observacao = models.CharField(max_length=300, blank=True)

#Classe abstrata para heran�a de classes que tenham apenas no nome
class SimpleClass(models.Model):
	nome = models.CharField(max_length=50)
	def __unicode__(self):
		return self.nome
	class Meta:
		abstract = True

class AtividadeFisica(SimpleClass):
	pass

class Doenca(SimpleClass):
	pass

class Cirurgia(SimpleClass):
	pass

class Medicacao(SimpleClass):
	pass

class Historico(models.Model):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	atividades_fisicas = models.ManyToManyField(AtividadeFisica, blank=True)
	doencas = models.ManyToManyField(Doenca, related_name='historicodoenca', blank=True)
	historico_familiar_doencas = models.ManyToManyField(Doenca, related_name='historicodoencafamiliar', blank=True)
	cirurgias = models.ManyToManyField(Cirurgia, blank=True)
	medicacoes = models.ManyToManyField(Medicacao, blank=True)
	observacao = models.CharField(max_length=300, blank=True)


class FormularioPARQ(models.Model):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	p1 = models.NullBooleanField(default=False)
	p2 = models.NullBooleanField(default=False)
	p3 = models.NullBooleanField(default=False)
	p4 = models.NullBooleanField(default=False)
	p5 = models.NullBooleanField(default=False)
	p6 = models.NullBooleanField(default=False)
	p7 = models.NullBooleanField(default=False)


class DadosVitais(models.Model):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	frequencia_cardiaca = models.IntegerField(null=True, blank=True)
	pa_sistole = models.IntegerField(null=True, blank=True)
	pa_diastole = models.IntegerField(null=True, blank=True)


class Antropometria(models.Model):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	observacao = models.CharField(max_length=300, blank=True)


class Circunferencias(models.Model):
	antropometria = models.OneToOneField(Antropometria, primary_key=True)
	pescoco = models.IntegerField(null=True, blank=True)
	ombros = models.IntegerField(null=True, blank=True)
	torax_relaxado = models.IntegerField(null=True, blank=True)
	torax_contraido = models.IntegerField(null=True, blank=True)
	biceps_direito_relaxado = models.IntegerField(null=True, blank=True)
	biceps_direito_contraido = models.IntegerField(null=True, blank=True)
	biceps_esquerdo_relaxado = models.IntegerField(null=True, blank=True)
	biceps_esquerdo_contraido = models.IntegerField(null=True, blank=True)
	cintura = models.IntegerField(null=True, blank=True)
	abdomen = models.IntegerField(null=True, blank=True)
	quadril = models.IntegerField(null=True, blank=True)
	coxa_direita = models.IntegerField(null=True, blank=True)
	coxa_esquerda = models.IntegerField(null=True, blank=True)
	panturrilha_direita = models.IntegerField(null=True, blank=True)
	panturrilha_esquerda = models.IntegerField(null=True, blank=True)

class PesoAltura(models.Model):
	antropometria = models.OneToOneField(Antropometria, primary_key=True)
	peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	altura = models.IntegerField(blank=True, null=True)