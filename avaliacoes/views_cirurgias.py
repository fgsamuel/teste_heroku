# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from avaliacoes.forms import CirurgiaForm
from avaliacoes.models import Cirurgia


def cirurgias_listar(request):
    if request.method == 'POST':
        busca = request.POST.get("busca", None)
        if busca != None:
            cirurgias = Cirurgia.objects.filter(nome__icontains=busca)
        else:
            cirurgias = Cirurgia.objects.all()
    else:
        cirurgias = Cirurgia.objects.all()
    
    context = {'cirurgias': cirurgias}
    return render(request, 'avaliacoes/cirurgias/index.html', context)

def cirurgias_inserir(request):
    if request.method == 'POST':
        form = CirurgiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cirurgias_listar")    
    form = CirurgiaForm()
    context = {'form' : form}
    return render(request, 'avaliacoes/cirurgias/inserir.html', context)

def cirurgias_editar(request, pk):
    try:
        cirurgia = Cirurgia.objects.get(pk=pk)
    except:
        cirurgia = None
    if request.method == 'POST':
        # para editar ele tem que receber a pessoa que está editando no parametro instance
        form = CirurgiaForm(request.POST, instance=cirurgia)
        if form.is_valid():
            form.save()
            return redirect("cirurgias_listar")
    else:
        # inicia o form com os dados da pessoa buscada
        form = CirurgiaForm(instance=cirurgia)
    context = {
        'cirurgia' : cirurgia,
        'form' : form
        }
    return render(request, 'avaliacoes/cirurgias/editar.html', context)

def cirurgias_excluir(request, pk):
    try:
        cirurgia = Cirurgia.objects.get(pk=pk)
    except:
        cirurgia = None
    if request.method == 'POST':
        cirurgia.delete()
        return redirect("cirurgias_listar")
    else:
        context = {'cirurgia' : cirurgia}
        return render(request, 'avaliacoes/cirurgias/excluir.html', context)