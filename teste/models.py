# -*- coding: utf-8 -*-

from django.db import models

class AtividadeFisica(models.Model):
	nome = models.CharField(max_length=50)

class Doenca(models.Model):
	nome = models.CharField(max_length=50)

class Cirurgia(models.Model):
	nome = models.CharField(max_length=50)

class Historico(models.Model):
	observacao = models.CharField(max_length=50)
	atividades_fisicas = models.ManyToManyField(AtividadeFisica)
	doencas = models.ManyToManyField(Doenca, related_name='historicodoenca')
	historico_familiar_doencas = models.ManyToManyField(Doenca, related_name='historicodoencafamiliar')
	cirurgias = models.ManyToManyField(Cirurgia)


