# -*- coding: utf-8 -*-

from django.forms import ModelForm, DateTimeInput
from avaliacoes.models import Historico

class HistoricoForm(ModelForm):
	class Meta:
		model = Historico
		fields = '__all__'