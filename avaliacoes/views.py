from django.shortcuts import render
from avaliacoes.forms import HistoricoForm

def avaliacoes(request):
	form = HistoricoForm()
	context = {'form' : form}
	return render(request, 'index.html', context)