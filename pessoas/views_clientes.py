# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from pessoas.forms import ClienteForm
from pessoas.models import Cliente


def clientes(request):
	if request.method == 'POST':
		busca = request.POST.get("busca", None)
		if busca != None:
			pessoas = Cliente.objects.filter(nome__icontains=busca)
		else:
			pessoas = Cliente.objects.all()
	else:
		pessoas = Cliente.objects.all()
		
	context = {'pessoas': pessoas}
	return render(request, 'pessoas/clientes/index.html', context)

def clientes_inserir(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("pessoas_clientes")	
		else:
			context = {'form' : form}
			return render(request, 'pessoas/clientes/inserir.html', context)
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
			context = {'form' : form}
			return render(request, 'pessoas/clientes/inserir.html', context)
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