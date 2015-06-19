# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from pessoas import views as pessoas_view
from avaliacoes import views as avaliacoes_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'fisioProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #CLIENTES
    url(r'^clientes/$', pessoas_view.clientes, name="pessoas_clientes"),
    url(r'^clientes/inserir/$', pessoas_view.clientes_inserir, name="pessoas_clientes_inserir"),
    url(r'^clientes/editar/(?P<pessoaId>[0-9]+)/$', pessoas_view.clientes_editar, name="pessoas_clientes_editar"),
    url(r'^clientes/visualizar/(?P<pessoaId>[0-9]+)/$', pessoas_view.clientes_visualizar, name="pessoas_clientes_visualizar"),
    url(r'^clientes/excluir/(?P<pessoaId>[0-9]+)/$', pessoas_view.clientes_excluir, name="pessoas_clientes_excluir"),


    #AVALIADORES
    url(r'^avaliadores/$', pessoas_view.avaliadores, name="pessoas_avaliadores"),
    url(r'^avaliadores/inserir/$', pessoas_view.avaliadores_inserir, name="pessoas_avaliadores_inserir"),
    url(r'^avaliadores/editar/(?P<pessoaId>[0-9]+)/$', pessoas_view.avaliadores_editar, name="pessoas_avaliadores_editar"),
    url(r'^avaliadores/visualizar/(?P<pessoaId>[0-9]+)/$', pessoas_view.avaliadores_visualizar, name="pessoas_avaliadores_visualizar"),
    url(r'^avaliadores/excluir/(?P<pessoaId>[0-9]+)/$', pessoas_view.avaliadores_excluir, name="pessoas_avaliadores_excluir"),

    #AVALIAÇÕES
    url(r'^avaliacoes/$', avaliacoes_view.avaliacoes, name="avaliacoes"),

    url(r'^doencas/$', avaliacoes_view.doencas_listar, name="doencas_listar"),
    url(r'^doencas/inserir/$', avaliacoes_view.doencas_inserir, name="doencas_inserir"),
    url(r'^doencas/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.doencas_editar, name="doencas_editar"),
    url(r'^doencas/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.doencas_excluir, name="doencas_excluir"),
    
    url(r'^atividades_fisicas/$', avaliacoes_view.atividades_fisicas_listar, name="atividades_fisicas_listar"),
    url(r'^atividades_fisicas/inserir/$', avaliacoes_view.atividades_fisicas_inserir, name="atividades_fisicas_inserir"),
    url(r'^atividades_fisicas/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.atividades_fisicas_editar, name="atividades_fisicas_editar"),
    url(r'^atividades_fisicas/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.atividades_fisicas_excluir, name="atividades_fisicas_excluir"),
    
    url(r'^cirurgias/$', avaliacoes_view.cirurgias_listar, name="cirurgias_listar"),
    url(r'^cirurgias/inserir/$', avaliacoes_view.cirurgias_inserir, name="cirurgias_inserir"),
    url(r'^cirurgias/editar/(?P<pk>[0-9]+)/$', avaliacoes_view.cirurgias_editar, name="cirurgias_editar"),
    url(r'^cirurgias/excluir/(?P<pk>[0-9]+)/$', avaliacoes_view.cirurgias_excluir, name="cirurgias_excluir"),
]
