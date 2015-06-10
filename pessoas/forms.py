# -*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput
from pessoas.models import Cliente, Avaliador

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'
		widgets = {
	            'data_nascimento': TextInput(attrs={'class': 'datepicker'}),
	        }

class AvaliadorForm(ModelForm):
	class Meta:
		model = Avaliador
		fields = '__all__'
		widgets = {
	            'data_nascimento': TextInput(attrs={'class': 'datepicker'}),
	        }
		