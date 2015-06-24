# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from pessoas.forms import AvaliadorForm
from pessoas.models import Avaliador


def avaliadores(request):
    if request.method == 'POST':
        busca = request.POST.get("busca", None)
        if busca != None:
            pessoas = Avaliador.objects.filter(nome__icontains=busca)
        else:
            pessoas = Avaliador.objects.all()
    else:
        pessoas = Avaliador.objects.all()
        
    context = {'pessoas': pessoas}
    return render(request, 'pessoas/avaliadores/index.html', context)

def avaliadores_inserir(request):
    if request.method == 'POST':
        form = AvaliadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pessoas_avaliadores")
        else:
            context = {'form' : form}
            return render(request, 'pessoas/avaliadores/inserir.html', context)
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
            context = {'form' : form}
            return render(request, 'pessoas/avaliadores/inserir.html', context)
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