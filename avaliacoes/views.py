# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from avaliacoes.forms import AvaliacaoForm, HistoricoForm, FormularioPARQForm, DadosVitaisForm,\
	CircunferenciasForm, PesoAlturaForm
import json


def avaliacoes(request):
	if request.method == 'POST': # If the form has been submitted...
			avaliacaoForm = AvaliacaoForm(request.POST, prefix="avaliacao")
			historicoForm = HistoricoForm(request.POST, prefix="historico")
			parqForm = FormularioPARQForm(request.POST, prefix="parq")
			dadosVitaisForm = DadosVitaisForm(request.POST, prefix="dadosvitais")
			circunferenciasForm = CircunferenciasForm(request.POST, prefix="circunferencias")
			pesoAlturaForm = PesoAlturaForm(request.POST, prefix="pesoAltura")

# 			
# 			if avaliacaoForm.is_valid() and historicoForm.is_valid() and parqForm.is_valid() and dadosVitaisForm.is_valid() and circunferenciasForm.is_valid() and pesoAlturaForm.is_valid():
# 				#salva a avaliação no banco para poder salvar os filhos
# 				avaliacao = avaliacaoForm.save()
# 
# 				#forma de salar relacionamentos many-to-many
# 				historico = historicoForm.save(commit=False)
# 				historico.avaliacao = avaliacao
# 				historico.save()
# 				historicoForm.save_m2m()
# 
# 				parq = parqForm.save(commit=False)
# 				parq.avaliacao = avaliacao
# 				parq.save()
# 
# 				dadosVitais = dadosVitaisForm.save(commit=False)
# 				dadosVitais.avaliacao = avaliacao
# 				dadosVitais.save()
# 
# 				circunferencias = circunferenciasForm.save(commit=False)
# 				circunferencias.avaliacao = avaliacao
# 				circunferencias.save()
# 
# 				pesoAltura = pesoAlturaForm.save(commit=False)
# 				pesoAltura.avaliacao = avaliacao
# 				pesoAltura.save()
# 				
# 				return redirect("pessoas_clientes")

			if historicoForm.is_valid():
				print(historicoForm.cleaned_data)
# 				var2 = json.dumps(historicoForm.cleaned_data)
# 				obj = json.loads(var2)
				
				for k, v in historicoForm.cleaned_data.items():
					if v:
						print("tem {}".format(k))
					else:
						print("Não tem {}".format(k))
				
# 				for k, v in obj.iteritems():
# 					if v:
# 						print("tem {}".format(k))
# 					else:
# 						print("Não tem {}".format(k))

				
	else:
		avaliacaoForm = AvaliacaoForm(prefix="avaliacao")
		historicoForm = HistoricoForm(prefix="historico")
		parqForm = FormularioPARQForm(prefix="parq")
		dadosVitaisForm = DadosVitaisForm(prefix="dadosvitais")
		circunferenciasForm = CircunferenciasForm(prefix="circunferencias")
		pesoAlturaForm = PesoAlturaForm(prefix="pesoAltura")
	context = {
		'avaliacaoForm' : avaliacaoForm,
		'historicoForm' : historicoForm,
		'parqForm' : parqForm,
		'dadosVitaisForm' : dadosVitaisForm,
		'circunferenciasForm' : circunferenciasForm,
		'pesoAlturaForm' : pesoAlturaForm,
		}
	return render(request, 'index.html', context)