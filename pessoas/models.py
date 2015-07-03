# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
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
	
	#nome da classe no singular
	def verbose(self):
		return self._meta.verbose_name.title()
	#nome da classe no plural
	def verbose_plural(self):
		return self._meta.verbose_name_plural.title()
	
	def __unicode__(self):
		return self.nome
	
	'''
	Sequência de métodos para obter as urls do crud, definidas em cada modelo pelo reverse()
	'''
	def url_index(self):
		return reverse(self.index)

	def url_inserir(self):
		return reverse(self.inserir)
	
	def url_editar(self):
		if self.pk:
			return reverse(self.editar, kwargs={'pessoaId':self.pk})
		else:
			return ""
	
	def url_visualizar(self):
		if self.pk:
			return reverse(self.visualizar, kwargs={'pessoaId':self.pk})
		else:
			return ""
	
	def url_excluir(self):
		if self.pk:
			return reverse(self.excluir, kwargs={'pessoaId':self.pk})
		else:
			return ""
		
	# para não ser persistida no banco
	class Meta:
		abstract = True
		ordering = ['nome']


class Cliente(Pessoa):
	index = 'pessoas_clientes'
	inserir = 'pessoas_clientes_inserir'
	editar = 'pessoas_clientes_editar'
	visualizar = 'pessoas_clientes_visualizar'
	excluir = 'pessoas_clientes_excluir'
	
	def form(self):
		from pessoas.forms import ClienteForm
		return ClienteForm
	def telefone_form(self):
		from pessoas.forms import TelefoneClienteForm
		return TelefoneClienteForm
	
class Avaliador(Pessoa):
	index = 'pessoas_avaliadores'
	inserir = 'pessoas_avaliadores_inserir'
	editar = 'pessoas_avaliadores_editar'
	visualizar = 'pessoas_avaliadores_visualizar'
	excluir = 'pessoas_avaliadores_excluir'
	
	def form(self):
		from pessoas.forms import AvaliadorForm
		return AvaliadorForm
	def telefone_form(self):
		from pessoas.forms import TelefoneAvaliadorForm
		return TelefoneAvaliadorForm
	
	
	class Meta:
		#o plural dele vem errado de acordo com a lingua portuguesa
		verbose_name_plural = 'Avaliadores'


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