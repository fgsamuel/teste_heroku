# -*- coding: utf-8 -*-

import json

from django.forms.formsets import formset_factory
from django.http.response import HttpResponse

from avaliacoes.forms import AvaliacaoForm, HistoricoForm, FormularioPARQForm, DadosVitaisForm, \
	CircunferenciasForm, PesoAlturaForm, PlicometriaForm, ObjetivosForm, \
	ImagemPosturalForm
from avaliacoes.models import ImagemPostural
from views_simpleClass import *


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
		print('é get')
		form = Formulario()
		return render(request, 'teste2.html', {'form': form})
	
	
def teste(request):
	if request.method == 'POST':
		form = DoencaForm(request.POST, prefix="doenca")
		if form.is_valid():
			# doenca = doencaForm.save()
			# data = {'return':0, 'obj' : {'id': doenca.pk, 'nome' : doenca.nome}}
			data = {'return':0, 'obj' : {'id': 17, 'nome' : "NOME QUALQUER"}}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			html = str(render(request, 'teste2.html', {'form': form}))
			print('primeiro')
			print(html)
			index = html.find('<')
			html = html[index:]
			print('segundo')
			print(html)
			data = {'return':1, 'html':html}
			print('data')
			print(data)
			return HttpResponse(json.dumps(data), content_type="application/json")

	doencaForm = DoencaForm(prefix='doenca')
	historicoForm = HistoricoForm(prefix='historico')
	return render(request, 'teste1.html', {'doencaForm':doencaForm, 'historicoForm':historicoForm})


def avaliacoes(request):
	if request.method == 'POST': # If the form has been submitted...
			avaliacaoForm = AvaliacaoForm(request.POST, prefix="avaliacao")
			historicoForm = HistoricoForm(request.POST, prefix="historico")
			parqForm = FormularioPARQForm(request.POST, prefix="parq")
			dadosVitaisForm = DadosVitaisForm(request.POST, prefix="dadosvitais")
			circunferenciasForm = CircunferenciasForm(request.POST, prefix="circunferencias")
			pesoAlturaForm = PesoAlturaForm(request.POST, prefix="pesoAltura")
			plicometriaForm = PlicometriaForm(request.POST, prefix="plicometria")
			objetivosForm = ObjetivosForm(request.POST, prefix="objetivos")

			
			if avaliacaoForm.is_valid() \
			and historicoForm.is_valid() \
			and parqForm.is_valid() \
			and dadosVitaisForm.is_valid() \
			and circunferenciasForm.is_valid() \
			and pesoAlturaForm.is_valid() \
			and plicometriaForm.is_valid() \
			and objetivosForm.is_valid():
				#salva a avaliação no banco primeiro para poder salvar os filhos
				avaliacao = avaliacaoForm.save()

				
				if historicoForm.is_empty() == False:
					historico = historicoForm.save(commit=False)
					historico.avaliacao = avaliacao
					historico.save()
					historicoForm.save_m2m()
				
				if objetivosForm.is_empty() == False:
					objetivos = objetivosForm.save(commit=False)
					objetivos.avaliacao = avaliacao
					objetivos.save()

				if parqForm.is_empty() == False:
					parq = parqForm.save(commit=False)
					parq.avaliacao = avaliacao
					parq.save()

				if dadosVitaisForm.is_empty() == False:
					dadosVitais = dadosVitaisForm.save(commit=False)
					dadosVitais.avaliacao = avaliacao
					dadosVitais.save()

				if circunferenciasForm.is_empty() == False:
					circunferencias = circunferenciasForm.save(commit=False)
					circunferencias.avaliacao = avaliacao
					circunferencias.save()

				if pesoAlturaForm.is_empty() == False:
					pesoAltura = pesoAlturaForm.save(commit=False)
					pesoAltura.avaliacao = avaliacao
					pesoAltura.save()
					
				if plicometriaForm.is_empty() == False:
					plicometria = plicometriaForm.save(commit=False)
					plicometria.avaliacao = avaliacao
					plicometria.save()
				
				return redirect("pessoas_clientes")
	else:
		avaliacaoForm = AvaliacaoForm(prefix="avaliacao")
		historicoForm = HistoricoForm(prefix="historico")
		parqForm = FormularioPARQForm(prefix="parq")
		dadosVitaisForm = DadosVitaisForm(prefix="dadosvitais")
		circunferenciasForm = CircunferenciasForm(prefix="circunferencias")
		pesoAlturaForm = PesoAlturaForm(prefix="pesoAltura")
		plicometriaForm = PlicometriaForm(prefix="plicometria")
		objetivosForm = ObjetivosForm(prefix="objetivos")
	context = {
		'avaliacaoForm' : avaliacaoForm,
		'historicoForm' : historicoForm,
		'parqForm' : parqForm,
		'dadosVitaisForm' : dadosVitaisForm,
		'circunferenciasForm' : circunferenciasForm,
		'pesoAlturaForm' : pesoAlturaForm,
		'plicometriaForm' : plicometriaForm,
		'objetivosForm' : objetivosForm,
		}
	return render(request, 'index.html', context)



def imagens(request):
	ImagemPosturalFormSet = formset_factory(ImagemPosturalForm, extra=4)
	forms = ImagemPosturalFormSet()
	# Handle file upload
	if request.method == 'POST':
		forms = ImagemPosturalFormSet(request.POST, request.FILES)
		if forms.is_valid():
			print("Válido")
		else:
			print("Inválido")

	
	# Load documents for the list page
	lista = ImagemPostural.objects.all()

	# Render list page with the documents and the form
	return render(request, 'imagens.html', {'lista':lista, 'forms':forms})
