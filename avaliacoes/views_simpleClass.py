# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from avaliacoes.forms import DoencaForm
from avaliacoes.models import Doenca


def listar(request, Classe):
    obj = Classe()
    if request.method == 'POST':
        busca = request.POST.get("busca", None)
        if busca != None:
            lista = Classe.objects.filter(nome__icontains=busca)
        else:
            lista = Classe.objects.all()
    else:
        lista = Classe.objects.all()
    
    context = {'lista': lista, 'obj': obj}
    return render(request, 'avaliacoes/simpleClass/index.html', context)

def inserir(request, Classe):
    obj = Classe()
    objForm = obj.form()

    if request.method == 'POST':
        form = objForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(obj.index)    
    form = objForm()
    context = {'form' : form, 'obj': obj}
    return render(request, 'avaliacoes/simpleClass/inserir.html', context)

def editar(request, pk, Classe):
    obj = Classe()
    objForm = obj.form()

    try:
        obj = Classe.objects.get(pk=pk)
    except:
        obj = None
    if request.method == 'POST':
        form = objForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(obj.index)
    else:
        # inicia o form com os dados da pessoa buscada
        form = DoencaForm(instance=obj)
    context = {
        'obj' : obj,
        'form' : form
        }
    return render(request, 'avaliacoes/simpleClass/editar.html', context)

def excluir(request, pk, Classe):
    obj = Classe()

    try:
        obj = Classe.objects.get(pk=pk)
    except:
        obj = None
    if request.method == 'POST':
        obj.delete()
        return redirect(obj.index)
    else:
        context = {'obj' : obj}
        return render(request, 'avaliacoes/simpleClass/excluir.html', context)

