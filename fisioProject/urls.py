# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from pessoas import views as pessoas_view

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
]
