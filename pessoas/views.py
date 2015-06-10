# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.shortcuts import render

from pessoas.forms import ClienteForm, AvaliadorForm
from pessoas.models import Cliente, Avaliador


def clientes(request):
	pessoas = Cliente.objects.all()
	context = {'pessoas': pessoas}
	return render(request, 'pessoas/clientes/index.html', context)

def clientes_inserir(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("pessoas_clientes")	
	form = ClienteForm()
	context = {'form' : form}
	return render(request, 'pessoas/clientes/inserir.html', context)


def clientes_editar(request, pessoaId):
	# Tenta encontrar a pessoa com o id passado, se não tiver, coloca None, e na view, quando recebe none, fala que não encontrou o cliente
	try:
		pessoa = Cliente.objects.get(pk=pessoaId)
	except:
		pessoa = None
	if request.method == 'POST':
		# para editar ele tem que receber a pessoa que está editando no parametro instance
		form = ClienteForm(request.POST, instance=pessoa)
		if form.is_valid():
			form.save()
			return redirect("pessoas_clientes")
	else:
		# inicia o form com os dados da pessoa buscada
		form = ClienteForm(instance=pessoa)
	context = {
		'pessoa' : pessoa,
		'form' : form
		}
	return render(request, 'pessoas/clientes/editar.html', context)

def clientes_visualizar(request, pessoaId):
	# Tenta encontrar a pessoa com o id passado, se não tiver, coloca None, e na view, quando recebe none, fala que não encontrou o cliente
	try:
		pessoa = Cliente.objects.get(pk=pessoaId)
	except:
		pessoa = None	
	context = {'pessoa' : pessoa}	
	return render(request, 'pessoas/clientes/visualizar.html', context)


def clientes_excluir(request, pessoaId):
	try:
		pessoa = Cliente.objects.get(pk=pessoaId)
	except:
		pessoa = None
	if request.method == 'POST':
		pessoa.delete()
		return redirect("pessoas_clientes")
	else:
		context = {'pessoa' : pessoa}
		return render(request, 'pessoas/clientes/excluir.html', context)
	
def avaliadores(request):
	pessoas = Avaliador.objects.all()
	context = {'pessoas': pessoas}
	return render(request, 'pessoas/avaliadores/index.html', context)

def avaliadores_inserir(request):
	if request.method == 'POST':
		form = AvaliadorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("pessoas_avaliadores")	
	form = AvaliadorForm()
	context = {'form' : form}
	return render(request, 'pessoas/avaliadores/inserir.html', context)


def avaliadores_editar(request, pessoaId):
	# Tenta encontrar a pessoa com o id passado, se não tiver, coloca None, e na view, quando recebe none, fala que não encontrou o avaliador
	try:
		pessoa = Avaliador.objects.get(pk=pessoaId)
	except:
		pessoa = None
	if request.method == 'POST':
		# para editar ele tem que receber a pessoa que está editando no parametro instance
		form = AvaliadorForm(request.POST, instance=pessoa)
		if form.is_valid():
			form.save()
			return redirect("pessoas_avaliadores")
	else:
		# inicia o form com os dados da pessoa buscada
		form = AvaliadorForm(instance=pessoa)
	context = {
		'pessoa' : pessoa,
		'form' : form
		}
	return render(request, 'pessoas/avaliadores/editar.html', context)

def avaliadores_visualizar(request, pessoaId):
	# Tenta encontrar a pessoa com o id passado, se não tiver, coloca None, e na view, quando recebe none, fala que não encontrou o avaliador
	try:
		pessoa = Avaliador.objects.get(pk=pessoaId)
	except:
		pessoa = None	
	context = {'pessoa' : pessoa}	
	return render(request, 'pessoas/avaliadores/visualizar.html', context)


def avaliadores_excluir(request, pessoaId):
	try:
		pessoa = Avaliador.objects.get(pk=pessoaId)
	except:
		pessoa = None
	if request.method == 'POST':
		pessoa.delete()
		return redirect("pessoas_avaliadores")
	else:
		context = {'pessoa' : pessoa}
		return render(request, 'pessoas/avaliadores/excluir.html', context)