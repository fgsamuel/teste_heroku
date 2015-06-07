# -*- coding: utf-8 -*-

from django.forms import ModelForm
from pessoas.models import Cliente

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente 
		fields = '__all__'
	def salvar(self):
		nome = self.cleaned_data.get('nome')
		c = Cliente(nome=nome)
		c.save()
		return c