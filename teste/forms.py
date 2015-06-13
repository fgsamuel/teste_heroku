# -*- coding: utf-8 -*-

from django.forms import ModelForm
from teste.models import Teste

class TesteForm(ModelForm):
	class Meta:
		model = Teste
		fields = '__all__'