# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models

from pessoas.models import Avaliador, Cliente

class GenericModel(models.Model):
	def get_fields(self):
		return self._meta.get_fields()
	class Meta:
		abstract = True


#-------------- Classes básicas do sistema------------------
#Classe abstrata para herança de classes que tenham apenas no nome
class SimpleClass(models.Model):
	nome = models.CharField(max_length=50)
	def __unicode__(self):
		return self.nome
	class Meta:
		abstract = True
		ordering = ['nome']
	#nome da classe no singular
	def verbose(self):
		return self._meta.verbose_name.title()
	#nome da classe no plural
	def verbose_plural(self):
		return self._meta.verbose_name_plural.title()
	
	'''
	Sequência de métodos para obter as urls do crud, definidas em cada modelo pelo reverse()
	'''
	def url_index(self):
		return reverse(self.index)

	def url_inserir(self):
		return reverse(self.inserir)
	
	def url_editar(self):
		if self.pk:
			return reverse(self.editar, kwargs={'pk':self.pk})
		else:
			return ""
	
	def url_visualizar(self):
		if self.pk:
			return reverse(self.visualizar, kwargs={'pk':self.pk})
		else:
			return ""
	
	def url_excluir(self):
		if self.pk:
			return reverse(self.excluir, kwargs={'pk':self.pk})
		else:
			return ""
		

class AtividadeFisica(SimpleClass):
	index = 'atividades_fisicas_listar'
	inserir = 'atividades_fisicas_inserir'
	editar = 'atividades_fisicas_editar'
	visualizar = 'atividades_fisicas_visualizar'
	excluir = 'atividades_fisicas_excluir'
	
	def form(self):
		from avaliacoes.forms import AtividadeFisicaForm
		return AtividadeFisicaForm
	
	class Meta:
		verbose_name_plural = u'Atividades Físicas'
		verbose_name = u"Atividade Física"

class Doenca(SimpleClass):
	index = 'doencas_listar'
	inserir = 'doencas_inserir'
	editar = 'doencas_editar'
	visualizar = 'doencas_visualizar'
	excluir = 'doencas_excluir'
	
	def form(self):
		from avaliacoes.forms import DoencaForm
		return DoencaForm
	
	class Meta:
		verbose_name_plural = u'Doenças'
		verbose_name = u"Doença"


class Cirurgia(SimpleClass):
	index = 'cirurgias_listar'
	inserir = 'cirurgias_inserir'
	editar = 'cirurgias_editar'
	visualizar = 'cirurgias_visualizar'
	excluir = 'cirurgias_excluir'
	
	def form(self):
		from avaliacoes.forms import CirurgiaForm
		return CirurgiaForm

class Medicacao(SimpleClass):
	index = 'medicacoes_listar'
	inserir = 'medicacoes_inserir'
	editar = 'medicacoes_editar'
	visualizar = 'medicacoes_visualizar'
	excluir = 'medicacoes_excluir'
	
	def form(self):
		from avaliacoes.forms import MedicacaoForm
		return MedicacaoForm
	
	class Meta:
		verbose_name_plural = u'Medicações'
		verbose_name = u"Medicação"


#Avaliação é a classe principal, através dela deve ser possível buscar todas as outras pelos relacionamentos
class Avaliacao(GenericModel):
	cliente = models.ForeignKey(Cliente)
	avaliador = models.ForeignKey(Avaliador)
	data = models.DateField()
	observacao = models.CharField(max_length=300, blank=True, verbose_name=u'Observação')
	def get_objetivos(self):
		if hasattr(self, 'objetivos'):
			return self.objetivos
		else:
			return None
	def get_historico(self):
		if hasattr(self, 'historico'):
			return self.historico
		else:
			return None
	def get_formularioparq(self):
		if hasattr(self, 'formularioparq'):
			return self.formularioparq
		else:
			return None
	def get_dadosvitais(self):
		if hasattr(self, 'dadosvitais'):
			return self.dadosvitais
		else:
			return None
	def get_circunferencias(self):
		if hasattr(self, 'circunferencias'):
			return self.circunferencias
		else:
			return None
	def get_pesoaltura(self):
		if hasattr(self, 'pesoaltura'):
			return self.pesoaltura
		else:
			return None
	def get_plicometria(self):
		if hasattr(self, 'plicometria'):
			return self.plicometria
		else:
			return None
	def get_fotos(self):
		if len(self.fotos.all()) > 0:
			return self.fotos
		else:
			return None


#----- as classes Objetivos e Historico fazem parte da Anamnese
class Objetivos(GenericModel):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	hipertrofia = models.BooleanField(blank=True)
	condicionamento_fisico = models.BooleanField(blank=True, verbose_name=u'Condicionamento Físico')
	diminuicao_percentual_gordura = models.BooleanField(blank=True, verbose_name=u'Redução do percentual de Gordura')
	melhorar_postura = models.BooleanField(blank=True)
	enrijecimento = models.BooleanField(blank=True)
	treino_forca = models.BooleanField(blank=True, verbose_name=u'Treino de força')
	flexibilidade = models.BooleanField(blank=True)
	observacao = models.CharField(max_length=300, blank=True, verbose_name=u'Observação')


class Historico(GenericModel):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	atividades_fisicas = models.ManyToManyField(AtividadeFisica, blank=True, verbose_name=u'Atividades Físicas')
	doencas = models.ManyToManyField(Doenca, related_name='historicodoenca', blank=True, verbose_name=u'Doenças')
	historico_familiar_doencas = models.ManyToManyField(Doenca, related_name='historicodoencafamiliar', blank=True, verbose_name=u'Histórico familiar de doenças')
	cirurgias = models.ManyToManyField(Cirurgia, blank=True)
	medicacoes = models.ManyToManyField(Medicacao, blank=True, verbose_name=u'Medicações')
	observacao = models.CharField(max_length=300, blank=True, verbose_name=u'Observação')



class FormularioPARQ(GenericModel):
	labels = {
            	'p1' : '1 - Seu médico já disse que você possui um problema cardíaco e recomendou atividades físicas apenas sob supervisão médica?',
				'p2' : '2 - Você tem dor no peito provocada por atividades físicas?',
				'p3' : '3 - Você sentiu dor no peito no último mês?',
				'p4' : '4 - Você já perdeu a consciência em alguma ocasião ou sofreu alguma queda em virtude de tontura?',
				'p5' : '5 - Você tem algum problema ósseo ou articular que poderia agravar-se com a prática de atividades físicas?',
				'p6' : '6 - Algum médico já lhe prescreveu medicamento para pressão arterial ou para o coração? ',
				'p7' : '7 - Você tem conhecimento, por informação médica ou pela própria experiência, de algum motivo que poderia impedí-lo de participar de atividades fisicas sem supervisão médica? ',
        }
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	p1 = models.NullBooleanField(default=False, verbose_name=labels['p1'])
	p2 = models.NullBooleanField(default=False, verbose_name=labels['p2'])
	p3 = models.NullBooleanField(default=False, verbose_name=labels['p3'])
	p4 = models.NullBooleanField(default=False, verbose_name=labels['p4'])
	p5 = models.NullBooleanField(default=False, verbose_name=labels['p5'])
	p6 = models.NullBooleanField(default=False, verbose_name=labels['p6'])
	p7 = models.NullBooleanField(default=False, verbose_name=labels['p7'])
	observacao = models.CharField(max_length=300, blank=True, verbose_name=u'Observação')


class DadosVitais(GenericModel):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	frequencia_cardiaca = models.IntegerField(null=True, blank=True, verbose_name=u'Frequência cardíaca')
	pa_sistole = models.IntegerField(null=True, blank=True, verbose_name=u'Pressão Arterial - Sistole')
	pa_diastole = models.IntegerField(null=True, blank=True, verbose_name=u'Pressão Arterial - Diastole')
	observacao = models.CharField(max_length=300, blank=True, verbose_name=u'Observação')
	

class Circunferencias(GenericModel):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	pescoco = models.IntegerField(null=True, blank=True, verbose_name=u'Pescoço')
	ombros = models.IntegerField(null=True, blank=True)
	torax_relaxado = models.IntegerField(null=True, blank=True, verbose_name=u'Tórax relaxado')
	torax_contraido = models.IntegerField(null=True, blank=True, verbose_name=u'Tórax contraído')
	biceps_direito_relaxado = models.IntegerField(null=True, blank=True, verbose_name=u'Bíceps direito relaxado')
	biceps_direito_contraido = models.IntegerField(null=True, blank=True, verbose_name=u'Bíceps direito contraído')
	biceps_esquerdo_relaxado = models.IntegerField(null=True, blank=True, verbose_name=u'Bíceps esquerdo relaxado')
	biceps_esquerdo_contraido = models.IntegerField(null=True, blank=True, verbose_name=u'Bíceps esquerdo contraído')
	cintura = models.IntegerField(null=True, blank=True)
	abdomen = models.IntegerField(null=True, blank=True)
	quadril = models.IntegerField(null=True, blank=True)
	coxa_direita = models.IntegerField(null=True, blank=True)
	coxa_esquerda = models.IntegerField(null=True, blank=True)
	panturrilha_direita = models.IntegerField(null=True, blank=True)
	panturrilha_esquerda = models.IntegerField(null=True, blank=True)
	observacao = models.CharField(max_length=300, blank=True, verbose_name=u'Observação')

class PesoAltura(GenericModel):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	altura = models.IntegerField(blank=True, null=True)
	observacao = models.CharField(max_length=300, blank=True, verbose_name=u'Observação')

class Plicometria(GenericModel):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	subscapular = models.IntegerField(null=True, blank=True)
	triceps_braquial = models.IntegerField(null=True, blank=True, verbose_name=u'Tríceps braquial')
	peitoral = models.IntegerField(null=True, blank=True)
	axilar_media = models.IntegerField(null=True, blank=True, verbose_name=u'Axiliar média')
	supra_iliaca = models.IntegerField(null=True, blank=True, verbose_name=u'Supra ilíaca')
	abdominal = models.IntegerField(null=True, blank=True)
	coxa = models.IntegerField(null=True, blank=True)
	panturrilha = models.IntegerField(null=True, blank=True)
	biciptal = models.IntegerField(null=True, blank=True)
	observacao = models.CharField(max_length=300, blank=True, verbose_name=u'Observação')

def get_file_name(instance, filename):
	return 'imagens_posturais/teste/foto.jpg'

class ImagemPostural(GenericModel):
	avaliacao = models.ForeignKey(Avaliacao, related_name='fotos')
	foto = models.ImageField(upload_to=get_file_name)
	descricao = models.CharField(max_length=100, verbose_name=u'Descrição')
	observacao = models.CharField(max_length=300, blank=True, verbose_name=u'Observação')
