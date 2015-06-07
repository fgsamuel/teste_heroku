# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import redirect

from pessoas.models import *
from pessoas.forms import *



def clientes(request):
	pessoas = Cliente.objects.all()
	context = {'pessoas': pessoas}
	return render(request, 'pessoas/clientes/index.html', context)

def clientes_editar(request, id):
	# Tenta encontrar a pessoa com o id passado, se não tiver, coloca None, e na view, quando recebe none, fala que não encontrou o cliente
	try:
		pessoa = Cliente.objects.get(pk=id)
	except:
		pessoa = None

	if request.method == 'POST':
		# para editar ele tem que receber a pessoa que está editando no parametro instance
		form = ClienteForm(request.POST, instance=pessoa)
		if form.is_valid():
			novo_cliente = form.save()
	else:
		# inicia o form com os dados da pessoa buscada
		form = ClienteForm(instance=pessoa)

	context = {
		'pessoa' : pessoa,
		'form' : form
		}
	return render(request, 'pessoas/clientes/editar.html', context)

def avaliadores(request):
	return render(request, 'pessoas/avaliadores/index.html')