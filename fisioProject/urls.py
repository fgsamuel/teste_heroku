# -*- coding: utf-8 -*-

from django.conf.urls import include, url, static
from django.contrib import admin

from avaliacoes import views as avaliacoes_view
from avaliacoes.forms import DoencaForm, AtividadeFisicaForm, MedicacaoForm, \
    CirurgiaForm
from avaliacoes.models import Doenca, AtividadeFisica, Cirurgia, Medicacao
from fisioProject import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'fisioProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^pessoas/', include('pessoas.urls')),

   
    #AVALIAÇÕES
    url(r'^avaliacoes/$', avaliacoes_view.avaliacoes, name="avaliacoes"),

    url(r'^doencas/$', avaliacoes_view.listar, {'Classe': Doenca}, name="doencas_listar"),
    url(r'^doencas/inserir/$', avaliacoes_view.inserir, {'Classe': Doenca}, name="doencas_inserir"),
    url(r'^doencas/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.editar, {'Classe': Doenca}, name="doencas_editar"),
    url(r'^doencas/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.excluir, {'Classe': Doenca}, name="doencas_excluir"),

    url(r'^atividades_fisicas/$', avaliacoes_view.listar, {'Classe': AtividadeFisica}, name="atividades_fisicas_listar"),
    url(r'^atividades_fisicas/inserir/$', avaliacoes_view.inserir, {'Classe': AtividadeFisica}, name="atividades_fisicas_inserir"),
    url(r'^atividades_fisicas/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.editar, {'Classe': AtividadeFisica}, name="atividades_fisicas_editar"),
    url(r'^atividades_fisicas/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.excluir, {'Classe': AtividadeFisica}, name="atividades_fisicas_excluir"),

    url(r'^cirurgias/$', avaliacoes_view.listar, {'Classe': Cirurgia}, name="cirurgias_listar"),
    url(r'^cirurgias/inserir/$', avaliacoes_view.inserir, {'Classe': Cirurgia}, name="cirurgias_inserir"),
    url(r'^cirurgias/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.editar, {'Classe': Cirurgia}, name="cirurgias_editar"),
    url(r'^cirurgias/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.excluir, {'Classe': Cirurgia}, name="cirurgias_excluir"),

    url(r'^medicacoes/$', avaliacoes_view.listar, {'Classe': Medicacao}, name="medicacoes_listar"),
    url(r'^medicacoes/inserir/$', avaliacoes_view.inserir, {'Classe': Medicacao}, name="medicacoes_inserir"),
    url(r'^medicacoes/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.editar, {'Classe': Medicacao}, name="medicacoes_editar"),
    url(r'^medicacoes/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.excluir, {'Classe': Medicacao}, name="medicacoes_excluir"),


    url(r'^teste/$', avaliacoes_view.teste, name="teste"),
    url(r'^avaliacoes/form_doenca$', avaliacoes_view.ajax_form, {'Formulario': DoencaForm}, name="form_ajax_doenca"),
    url(r'^avaliacoes/form_atividade_fisica', avaliacoes_view.ajax_form, {'Formulario': AtividadeFisicaForm}, name="form_ajax_atividade_fisica"),
    url(r'^avaliacoes/form_medicacao$', avaliacoes_view.ajax_form, {'Formulario': MedicacaoForm}, name="form_ajax_medicacao"),
    url(r'^avaliacoes/form_cirurgia$', avaliacoes_view.ajax_form, {'Formulario': CirurgiaForm}, name="form_ajax_cirurgia"),
    
    url(r'^imagens/$', avaliacoes_view.imagens, name="imagens"),
]
