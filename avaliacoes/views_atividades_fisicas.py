# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from avaliacoes.forms import AtividadeFisicaForm
from avaliacoes.models import AtividadeFisica


def atividades_fisicas_listar(request):
    if request.method == 'POST':
        busca = request.POST.get("busca", None)
        if busca != None:
            atividades_fisicas = AtividadeFisica.objects.filter(nome__icontains=busca)
        else:
            atividades_fisicas = AtividadeFisica.objects.all()
    else:
        atividades_fisicas = AtividadeFisica.objects.all()
    
    context = {'atividades_fisicas': atividades_fisicas}
    return render(request, 'avaliacoes/atividades_fisicas/index.html', context)

def atividades_fisicas_inserir(request):
    if request.method == 'POST':
        form = AtividadeFisicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("atividades_fisicas_listar")    
    form = AtividadeFisicaForm()
    context = {'form' : form}
    return render(request, 'avaliacoes/atividades_fisicas/inserir.html', context)

def atividades_fisicas_editar(request, pk):
    try:
        atividade_fisica = AtividadeFisica.objects.get(pk=pk)
    except:
        atividade_fisica = None
    if request.method == 'POST':
        # para editar ele tem que receber a pessoa que está editando no parametro instance
        form = AtividadeFisicaForm(request.POST, instance=atividade_fisica)
        if form.is_valid():
            form.save()
            return redirect("atividades_fisicas_listar")
    else:
        # inicia o form com os dados da pessoa buscada
        form = AtividadeFisicaForm(instance=atividade_fisica)
    context = {
        'atividade_fisica' : atividade_fisica,
        'form' : form
        }
    return render(request, 'avaliacoes/atividades_fisicas/editar.html', context)

def atividades_fisicas_excluir(request, pk):
    try:
        atividade_fisica = AtividadeFisica.objects.get(pk=pk)
    except:
        atividade_fisica = None
    if request.method == 'POST':
        atividade_fisica.delete()
        return redirect("atividades_fisicas_listar")
    else:
        context = {'atividade_fisica' : atividade_fisica}
        return render(request, 'avaliacoes/atividades_fisicas/excluir.html', context)