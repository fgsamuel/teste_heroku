# -*- coding: utf-8 -*-

from django.forms import ModelForm, DateTimeInput
from avaliacoes.models import Avaliacao, Historico, Anamnese, FormularioPARQ, DadosVitais, \
	Circunferencias, PesoAltura
from django.forms.widgets import SelectMultiple

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

class AnamneseForm(ModelForm):
	class Meta:
		model = Anamnese
		exclude = ('avaliacao',)

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


class DadosVitaisForm(ModelForm):
	class Meta:
		model = DadosVitais
		exclude = ('avaliacao',)

class CircunferenciasForm(ModelForm):
	class Meta:
		model = Circunferencias
		exclude = ('antropometria',)

class PesoAlturaForm(ModelForm):
	class Meta:
		model = PesoAltura
		exclude = ('antropometria',)