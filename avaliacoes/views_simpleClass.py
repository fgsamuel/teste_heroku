# -*- coding: utf-8 -*-
import json

from django.http.response import HttpResponse
from django.shortcuts import render, redirect


def simpleClass_listar(request, Classe):
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

def simpleClass_inserir(request, Classe):
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

def simpleClass_editar(request, pk, Classe):
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
        form = objForm(instance=obj)
    context = {
        'obj' : obj,
        'form' : form
        }
    return render(request, 'avaliacoes/simpleClass/editar.html', context)

def simpleClass_excluir(request, pk, Classe):
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


#retorna o form e o salva quando recebe via ajax
def ajax_form(request, Formulario):
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            obj = form.save()
            data = {'return':0, 'obj' : {'id': obj.pk , 'nome' : u'{}'.format(obj.nome) }}
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            html = str(render(request, 'teste2.html', {'form': form}))
            index = html.find('<')
            html = html[index:]
            data = {'return':1, 'html':html}
            return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        form = Formulario()
        return render(request, 'avaliacoes/simpleClass/form.html', {'form': form})