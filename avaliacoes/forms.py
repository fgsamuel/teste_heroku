# -*- coding: utf-8 -*-

from django.forms import ModelForm
from avaliacoes.models import Avaliacao, Historico, Anamnese

class AvaliacaoForm(ModelForm):
	class Meta:
		model = Avaliacao
		fields = '__all__'
		
class HistoricoForm(ModelForm):
	class Meta:
		model = Historico
		exclude = ('avaliacao',)

class AnamneseForm(ModelForm):
	class Meta:
		model = Anamnese
		exclude = ('avaliacao',)