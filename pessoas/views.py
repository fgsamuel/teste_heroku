# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.forms.formsets import formset_factory


def index(request, Classe):
    obj = Classe()
    txtBusca = ""
    if request.method == 'POST':
        txtBusca = request.POST.get("busca")
        if txtBusca.strip():
            pessoas = Classe.objects.filter(nome__icontains=txtBusca)
        else:
            pessoas = Classe.objects.all()
    else:
        pessoas = Classe.objects.all()
        
    context = {'pessoas': pessoas, 'obj':obj, 'busca':txtBusca}
    return render(request, 'pessoas/index.html', context)

def inserir(request, Classe):
    obj = Classe()
    objForm = obj.form()
    TelefoneForm = obj.telefone_form()
    FormSet = formset_factory(TelefoneForm, extra=1)
    if request.method == 'POST':
        form = objForm(request.POST)
        form_telefone = FormSet(request.POST)
        if form.is_valid() and form_telefone.is_valid():
            pessoa = form.save()
            
            for f in form_telefone:
                if f.has_changed():
                    telefone = f.save(commit=False)
                    telefone.pessoa = pessoa
                    telefone.save()
            
            return redirect(obj.index)    
        else:
            context = {'form' : form, 'obj':obj, 'telefonesForm':form_telefone}
            return render(request, 'pessoas/inserir.html', context)
    form = objForm()
    context = {'form' : form, 'obj':obj, 'telefonesForm':FormSet}
    return render(request, 'pessoas/inserir.html', context)

def editar(request, pessoaId, Classe):
    obj = Classe()
    objForm = obj.form()

    try:
        pessoa = Classe.objects.get(pk=pessoaId)
    except:
        pessoa = None

    if request.method == 'POST':
        # para editar ele tem que receber a pessoa que está editando no parametro instance
        form = objForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect(obj.index)
        else:
            context = {'form' : form, 'obj':obj}
            return render(request, 'pessoas/editar.html', context)
    else:
        # inicia o form com os dados da pessoa buscada
        form = objForm(instance=pessoa)
    context = {
        'pessoa' : pessoa,
        'form' : form,
        'obj' : obj,
        }
    return render(request, 'pessoas/editar.html', context)

def visualizar(request, pessoaId, Classe):
    obj = Classe()
    # Tenta encontrar a pessoa com o id passado, se não tiver, coloca None, e na view, quando recebe none, fala que não encontrou o cliente
    try:
        pessoa = Classe.objects.get(pk=pessoaId)
    except:
        pessoa = None    
    context = {'pessoa' : pessoa, 'obj':obj}    
    return render(request, 'pessoas/visualizar.html', context)

def excluir(request, pessoaId, Classe):
    obj = Classe()
    try:
        pessoa = Classe.objects.get(pk=pessoaId)
    except:
        pessoa = None
    if request.method == 'POST':
        pessoa.delete()
        return redirect(obj.index)
    else:
        context = {'pessoa' : pessoa, 'obj':obj}
        return render(request, 'pessoas/excluir.html', context)