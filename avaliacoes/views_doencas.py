# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from avaliacoes.forms import DoencaForm
from avaliacoes.models import Doenca


def doencas_listar(request):
    if request.method == 'POST':
        busca = request.POST.get("busca", None)
        if busca != None:
            doencas = Doenca.objects.filter(nome__icontains=busca)
        else:
            doencas = Doenca.objects.all()
    else:
        doencas = Doenca.objects.all()
    
    context = {'doencas': doencas}
    return render(request, 'avaliacoes/doencas/index.html', context)

def doencas_inserir(request):
    if request.method == 'POST':
        form = DoencaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("doencas_listar")    
    form = DoencaForm()
    context = {'form' : form}
    return render(request, 'avaliacoes/doencas/inserir.html', context)

def doencas_editar(request, pk):
    try:
        doenca = Doenca.objects.get(pk=pk)
    except:
        doenca = None
    if request.method == 'POST':
        # para editar ele tem que receber a pessoa que está editando no parametro instance
        form = DoencaForm(request.POST, instance=doenca)
        if form.is_valid():
            form.save()
            return redirect("doencas_listar")
    else:
        # inicia o form com os dados da pessoa buscada
        form = DoencaForm(instance=doenca)
    context = {
        'doenca' : doenca,
        'form' : form
        }
    return render(request, 'avaliacoes/doencas/editar.html', context)

def doencas_excluir(request, pk):
    try:
        doenca = Doenca.objects.get(pk=pk)
    except:
        doenca = None
    if request.method == 'POST':
        doenca.delete()
        return redirect("doencas_listar")
    else:
        context = {'doenca' : doenca}
        return render(request, 'avaliacoes/doencas/excluir.html', context)