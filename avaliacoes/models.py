from django.db import models
from pessoas.models import Avaliador, Cliente

class Avaliacao(models.Model):
	cliente = models.ForeignKey(Cliente)
	avaliador = models.ForeignKey(Avaliador)
	data = models.DateField()
	observacao = models.CharField(max_length=300)


class Anamnese(models.Model):
	avaliacao = models.OneToOneField(Avaliacao, primary_key=True)
	hipertrofia = models.BooleanField()
	condicionamento_fisico = models.BooleanField()
	diminuicao_percentual_gordura = models.BooleanField()
	melhorar_postura = models.BooleanField()
	enrijecimento = models.BooleanField()
	treino_forca = models.BooleanField()
	flexibilidade = models.BooleanField()
	observacao = models.CharField(max_length=300)

#Classe abstrata para heran�a de classes que tenham apenas no nome
class SimpleClass(models.Model):
	nome = models.CharField(max_length=50)
	def __unicode__(self):
		return self.nome
	class Meta:
		abstract = True

class AtividadeFisica(SimpleClass):
	pass

class Doenca(SimpleClass):
	pass

class Cirurgia(SimpleClass):
	pass

class Medicacao(SimpleClass):
	pass

class Historico(models.Model):
	atividades_fisicas = models.ManyToManyField(AtividadeFisica)
	doencas = models.ManyToManyField(Doenca, related_name='historicodoenca')
	historico_familiar_doencas = models.ManyToManyField(Doenca, related_name='historicodoencafamiliar')
	cirurgias = models.ManyToManyField(Cirurgia)
	observacao = models.CharField(max_length=300)

