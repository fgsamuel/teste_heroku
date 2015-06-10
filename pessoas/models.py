# -*- coding: utf-8 -*-

from django.db import models

# Classe abstrata para reunir todas informações comuns à pessoas
class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	data_nascimento = models.DateField(blank=True, null=True)
	email = models.CharField(max_length=150, blank=True)
	cep = models.CharField(max_length=8, blank=True)
	numero = models.CharField(max_length=10, blank=True)
	complemento = models.CharField(max_length=50, blank=True)
	observacao = models.CharField(max_length=300, blank=True)
	def __unicode__(self):
		return self.nome
	# para não ser persistida no banco
	class Meta:
		abstract = True


class Cliente(Pessoa):
	pass


class Avaliador(Pessoa):
	pass


class Telefone(models.Model):
	ddd = models.CharField(max_length=2)
	numero = models.CharField(max_length=9)
	observacao = models.CharField(max_length=300, blank=True)
	def __unicode__(self):
		#desta forma atende tanto número com 8 quanto com 9 dígitos
		return "({}){}-{}".format(self.ddd, self.numero[:-4], self.numero[-4:])

	# para não ser persistida no banco
	class Meta:
		abstract = True


class TelefoneCliente(Telefone):
	pessoa = models.ForeignKey(Cliente, related_name='telefones')

class TelefoneAvaliador(Telefone):
	pessoa = models.ForeignKey(Avaliador, related_name='telefones')