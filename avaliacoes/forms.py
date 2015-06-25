# -*- coding: utf-8 -*-

from django.forms import ModelForm, DateTimeInput
from django.forms.widgets import SelectMultiple

from avaliacoes.models import Avaliacao, Historico, FormularioPARQ, DadosVitais, Circunferencias, PesoAltura, \
	Plicometria, Objetivos, Doenca, AtividadeFisica, Cirurgia, Medicacao


class AvaliacaoForm(ModelForm):
	class Meta:
		model = Avaliacao
		fields = '__all__'
		widgets = {
		            'data': DateTimeInput(format='%d/%m/%Y', attrs={
										'class':'datepicker',
										'size':'10',
										'editable' : 'false'
									}),
	        		}

class ObjetivosForm(ModelForm):
	class Meta:
		model = Objetivos
		exclude = ('avaliacao',)
	def is_empty(self):
		return is_empty(self)
		
class HistoricoForm(ModelForm):
	class Meta:
		model = Historico
		exclude = ('avaliacao',)
		widgets = {
		            'atividades_fisicas': SelectMultiple(attrs={
										'class':'select2',
										'style':'width:500px',
										'data-placeholder': 'Selecione as atividades físicas'
									}),
		            'doencas': SelectMultiple(attrs={
										'class':'select2',
										'style':'width:350px',
										'data-placeholder': 'Selecione as doenças'
									}),
		            'historico_familiar_doencas': SelectMultiple(attrs={
										'class':'select2',
										'style':'width:500px',
										'data-placeholder': 'Selecione as doenças'
									}),
		            'medicacoes': SelectMultiple(attrs={
										'class':'select2',
										'style':'width:500px',
										'data-placeholder': 'Selecione as medicações'
									}),
		            'cirurgias': SelectMultiple(attrs={
										'class':'select2',
										'style':'width:500px',
										'data-placeholder': 'Selecione as cirurgias'
									}),
	        		}
	def is_empty(self):
		return is_empty(self)

class FormularioPARQForm(ModelForm):
	class Meta:
		model = FormularioPARQ
		exclude = ('avaliacao',)
		labels = {
            	'p1' : '1 - Seu médico já disse que você possui um problema cardíaco e recomendou atividades físicas apenas sob supervisão médica?',
				'p2' : '2 - Você tem dor no peito provocada por atividades físicas?',
				'p3' : '3 - Você sentiu dor no peito no último mês?',
				'p4' : '4 - Você já perdeu a consciência em alguma ocasião ou sofreu alguma queda em virtude de tontura?',
				'p5' : '5 - Você tem algum problema ósseo ou articular que poderia agravar-se com a prática de atividades físicas?',
				'p6' : '6 - Algum médico já lhe prescreveu medicamento para pressão arterial ou para o coração? ',
				'p7' : '7 - Você tem conhecimento, por informação médica ou pela própria experiência, de algum motivo que poderia impedí-lo de participar de atividades fisicas sem supervisão médica? ',
        }
	def is_empty(self):
		return is_empty(self)


class DadosVitaisForm(ModelForm):
	class Meta:
		model = DadosVitais
		exclude = ('avaliacao',)
	def is_empty(self):
		return is_empty(self)

class CircunferenciasForm(ModelForm):
	class Meta:
		model = Circunferencias
		exclude = ('avaliacao',)
	def is_empty(self):
		return is_empty(self)

class PesoAlturaForm(ModelForm):
	class Meta:
		model = PesoAltura
		exclude = ('avaliacao',)
	def is_empty(self):
		return is_empty(self)

class PlicometriaForm(ModelForm):
	class Meta:
		model = Plicometria
		exclude = ('avaliacao',)
	def is_empty(self):
		return is_empty(self)
		
'''
Este método recebe um form e o valida
após isso, ele pega o conteúdo deste form,
percorre tupla por tupla.
Se todoas estiverem vazias, retorna true
se pelo moenos uma estiver preenchida, retorna false
Se o form não passar na validação, retorna none.
'''
		
def is_empty(form):
	if form.is_valid():
		data = form.cleaned_data
		for k in data.items():
			if k[1]:
				return False
		return True
	else:
		return None



class DoencaForm(ModelForm):
	class Meta:
		model = Doenca
		fields = '__all__'

class AtividadeFisicaForm(ModelForm):
	class Meta:
		model = AtividadeFisica
		fields = '__all__'
		
class CirurgiaForm(ModelForm):
	class Meta:
		model = Cirurgia
		fields = '__all__'

class MedicacaoForm(ModelForm):
	class Meta:
		model = Medicacao
		fields = '__all__'
	
	
	
	
	