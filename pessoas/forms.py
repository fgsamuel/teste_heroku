# -*- coding: utf-8 -*-

from django.forms import ModelForm, DateTimeInput
from pessoas.models import Cliente, Avaliador

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'
		widgets = {
		            'data_nascimento': DateTimeInput(format='%d/%m/%Y', attrs={
										'class':'datepicker',
										'size':'10',
										'editable' : 'false'
									}),
	        		}

class AvaliadorForm(ModelForm):
	class Meta:
		model = Avaliador
		fields = '__all__'
		widgets = {
		            'data_nascimento': DateTimeInput(format='%d/%m/%Y', attrs={
										'class':'datepicker',
										'size':'10',
										'editable' : 'false'
									}),
	        		}
		