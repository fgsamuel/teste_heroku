# -*- coding: utf-8 -*-

import json

from django.http.response import HttpResponse

from avaliacoes.forms import AvaliacaoForm, HistoricoForm, FormularioPARQForm, DadosVitaisForm, \
	CircunferenciasForm, PesoAlturaForm, PlicometriaForm, ObjetivosForm, DoencaForm
from views_atividades_fisicas import *
from views_cirurgias import *
from views_doencas import *


def teste(request):
	if request.method == 'POST':
		print("method post")
		doencaForm = DoencaForm(request.POST, prefix="doenca")
		if doencaForm.is_valid():
			print("Valido")
			html = str(render(request, 'teste2.html', {'doencaForm': doencaForm}, content_type=""))
			index = html.find('<')
			html = html[index:]
			print(html)
			data = {'html':html, 'message':"Mensagem qualquer"}
			print(data)
			data2 = json.dumps(data)
			print(data2)
			return HttpResponse(data2, content_type="application/json")
		else:
			print("Invalido")
			html = str(render(request, 'teste2.html', {'doencaForm': doencaForm}))
			index = html.find('<')
			html = html[index:]
			data = {'html':html, 'message':"Mensagem qualquer"}
			print(data)
			data2 = json.dumps(data)
			print(data2)
			return HttpResponse(data2, content_type="application/json")
	doencaForm = DoencaForm(prefix="doenca")
	historicoForm = HistoricoForm(prefix="historico")
	return render(request, 'teste1.html', {'doencaForm': doencaForm, 'historicoForm':historicoForm})

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