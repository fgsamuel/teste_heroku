# -*- coding: utf-8 -*-

from django.conf.urls import url

from avaliacoes import views as avaliacoes_view
from avaliacoes.forms import DoencaForm, AtividadeFisicaForm, MedicacaoForm, CirurgiaForm
from avaliacoes.models import Doenca, AtividadeFisica, Cirurgia, Medicacao


urlpatterns = [

    
    url(r'^$', avaliacoes_view.avaliacoes_listar, name="avaliacoes_listar"),
    
    url(r'^inserir/$', avaliacoes_view.avaliacoes_inserir, name="avaliacoes_inserir"),
    url(r'^visualizar/(?P<pk>[0-9]+)/$', avaliacoes_view.avaliacoes_visualizar, name="avaliacoes_visualizar"),

    url(r'^doencas/$', avaliacoes_view.simpleClass_listar, {'Classe': Doenca}, name="doencas_listar"),
    url(r'^doencas/inserir/$', avaliacoes_view.simpleClass_inserir, {'Classe': Doenca}, name="doencas_inserir"),
    url(r'^doencas/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.simpleClass_editar, {'Classe': Doenca}, name="doencas_editar"),
    url(r'^doencas/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.simpleClass_excluir, {'Classe': Doenca}, name="doencas_excluir"),

    url(r'^atividades_fisicas/$', avaliacoes_view.simpleClass_listar, {'Classe': AtividadeFisica}, name="atividades_fisicas_listar"),
    url(r'^atividades_fisicas/inserir/$', avaliacoes_view.simpleClass_inserir, {'Classe': AtividadeFisica}, name="atividades_fisicas_inserir"),
    url(r'^atividades_fisicas/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.simpleClass_editar, {'Classe': AtividadeFisica}, name="atividades_fisicas_editar"),
    url(r'^atividades_fisicas/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.simpleClass_excluir, {'Classe': AtividadeFisica}, name="atividades_fisicas_excluir"),

    url(r'^cirurgias/$', avaliacoes_view.simpleClass_listar, {'Classe': Cirurgia}, name="cirurgias_listar"),
    url(r'^cirurgias/inserir/$', avaliacoes_view.simpleClass_inserir, {'Classe': Cirurgia}, name="cirurgias_inserir"),
    url(r'^cirurgias/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.simpleClass_editar, {'Classe': Cirurgia}, name="cirurgias_editar"),
    url(r'^cirurgias/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.simpleClass_excluir, {'Classe': Cirurgia}, name="cirurgias_excluir"),

    url(r'^medicacoes/$', avaliacoes_view.simpleClass_listar, {'Classe': Medicacao}, name="medicacoes_listar"),
    url(r'^medicacoes/inserir/$', avaliacoes_view.simpleClass_inserir, {'Classe': Medicacao}, name="medicacoes_inserir"),
    url(r'^medicacoes/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.simpleClass_editar, {'Classe': Medicacao}, name="medicacoes_editar"),
    url(r'^medicacoes/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.simpleClass_excluir, {'Classe': Medicacao}, name="medicacoes_excluir"),


    url(r'^form_doenca$', avaliacoes_view.ajax_form, {'Formulario': DoencaForm}, name="form_ajax_doenca"),
    url(r'^form_atividade_fisica', avaliacoes_view.ajax_form, {'Formulario': AtividadeFisicaForm}, name="form_ajax_atividade_fisica"),
    url(r'^form_medicacao$', avaliacoes_view.ajax_form, {'Formulario': MedicacaoForm}, name="form_ajax_medicacao"),
    url(r'^form_cirurgia$', avaliacoes_view.ajax_form, {'Formulario': CirurgiaForm}, name="form_ajax_cirurgia"),
    
    url(r'^imagens/$', avaliacoes_view.imagens, name="imagens"),
]
