# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from avaliacoes.forms import AvaliacaoForm, HistoricoForm, AnamneseForm, FormularioPARQForm, DadosVitaisForm,\
	CircunferenciasForm, PesoAlturaForm
from avaliacoes.models import Antropometria


def avaliacoes(request):
	if request.method == 'POST': # If the form has been submitted...
			avaliacaoForm = AvaliacaoForm(request.POST, prefix="avaliacao")
			historicoForm = HistoricoForm(request.POST, prefix="historico")
			anamneseForm = AnamneseForm(request.POST, prefix="anamnese")
			parqForm = FormularioPARQForm(request.POST, prefix="parq")
			dadosVitaisForm = DadosVitaisForm(request.POST, prefix="dadosvitais")
			circunferenciasForm = CircunferenciasForm(request.POST, prefix="circunferencias")
			pesoAlturaForm = PesoAlturaForm(request.POST, prefix="pesoAltura")

			
			if avaliacaoForm.is_valid() and historicoForm.is_valid() and anamneseForm.is_valid() and parqForm.is_valid() and dadosVitaisForm.is_valid() and circunferenciasForm.is_valid() and pesoAlturaForm.is_valid():
				#salva a avaliação no banco para poder salvar os filhos
				avaliacao = avaliacaoForm.save()

				#forma de salar relacionamentos many-to-many
				historico = historicoForm.save(commit=False)
				historico.avaliacao = avaliacao
				historico.save()
				historicoForm.save_m2m()

				anamnese = anamneseForm.save(commit=False)
				anamnese.avaliacao = avaliacao
				anamnese.save()

				parq = parqForm.save(commit=False)
				parq.avaliacao = avaliacao
				parq.save()

				dadosVitais = dadosVitaisForm.save(commit=False)
				dadosVitais.avaliacao = avaliacao
				dadosVitais.save()

				antropometria = Antropometria()
				antropometria.avaliacao = avaliacao
				antropometria.save()

				circunferencias = circunferenciasForm.save(commit=False)
				circunferencias.antropometria = antropometria
				circunferencias.save()

				pesoAltura = pesoAlturaForm.save(commit=False)
				pesoAltura.antropometria = antropometria
				pesoAltura.save()
				
				return redirect("pessoas_clientes")
	else:
		avaliacaoForm = AvaliacaoForm(prefix="avaliacao")
		historicoForm = HistoricoForm(prefix="historico")
		anamneseForm = AnamneseForm(prefix="anamnese")
		parqForm = FormularioPARQForm(prefix="parq")
		dadosVitaisForm = DadosVitaisForm(prefix="dadosvitais")
		circunferenciasForm = CircunferenciasForm(prefix="circunferencias")
		pesoAlturaForm = PesoAlturaForm(prefix="pesoAltura")
	context = {
		'avaliacaoForm' : avaliacaoForm,
		'historicoForm' : historicoForm,
		'anamneseForm' : anamneseForm,
		'parqForm' : parqForm,
		'dadosVitaisForm' : dadosVitaisForm,
		'circunferenciasForm' : circunferenciasForm,
		'pesoAlturaForm' : pesoAlturaForm,
		}
	return render(request, 'index.html', context)