from distutils.sysconfig import PREFIX

from django.shortcuts import render, redirect
from django.template.smartif import prefix

from avaliacoes.forms import AvaliacaoForm, HistoricoForm, AnamneseForm


def avaliacoes(request):
	if request.method == 'POST': # If the form has been submitted...
			avaliacaoForm = AvaliacaoForm(request.POST, prefix="avaliacao")
			historicoForm = HistoricoForm(request.POST, prefix="historico")
			anamneseForm = AnamneseForm(request.POST, prefix="anamnese")
			
			if avaliacaoForm.is_valid():
				print("avaliacao valido")
			else:
				print("avaliacao invalido")
			if historicoForm.is_valid():
				print("historico valido")
			else:
				print("historico invalido")
			if anamneseForm.is_valid():
				print("anamnese valido")
			else:
				print("anamnese invalido")
			if avaliacaoForm.is_valid() and historicoForm.is_valid() and anamneseForm.is_valid(): # All validation rules pass
				print("all validation passed")
				avaliacao = avaliacaoForm.save()
				historicoForm.cleaned_data["avaliacao"] = avaliacao
				historicoForm.save()
				anamneseForm.cleaned_data["avaliacao"] = avaliacao
				anamneseForm.save()
				return redirect("pessoas_clientes")
			else:
				print("failed")

	avaliacaoForm = AvaliacaoForm(prefix="avaliacao")
	historicoForm = HistoricoForm(prefix="historico")
	anamneseForm = AnamneseForm(prefix="anamnese")
	context = {
		'avaliacaoForm' : avaliacaoForm,
		'historicoForm' : historicoForm,
		'anamneseForm' : anamneseForm,
		}
	return render(request, 'index.html', context)