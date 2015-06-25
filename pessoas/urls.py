from django.conf.urls import url

from pessoas import views
from pessoas.models import Cliente, Avaliador


urlpatterns = [
 
 # CLIENTES
    url(r'^clientes/$', views.index, {'Classe': Cliente}, name="pessoas_clientes"),
    url(r'^clientes/inserir/$', views.inserir, {'Classe': Cliente}, name="pessoas_clientes_inserir"),
    url(r'^clientes/editar/(?P<pessoaId>[0-9]+)/$', views.editar, {'Classe': Cliente}, name="pessoas_clientes_editar"),
    url(r'^clientes/visualizar/(?P<pessoaId>[0-9]+)/$', views.visualizar, {'Classe': Cliente}, name="pessoas_clientes_visualizar"),
    url(r'^clientes/excluir/(?P<pessoaId>[0-9]+)/$', views.excluir, {'Classe': Cliente}, name="pessoas_clientes_excluir"),


    # AVALIADORES
    url(r'^avaliadores/$', views.index, {'Classe': Avaliador}, name="pessoas_avaliadores"),
    url(r'^avaliadores/inserir/$', views.inserir, {'Classe': Avaliador}, name="pessoas_avaliadores_inserir"),
    url(r'^avaliadores/editar/(?P<pessoaId>[0-9]+)/$', views.editar, {'Classe': Avaliador}, name="pessoas_avaliadores_editar"),
    url(r'^avaliadores/visualizar/(?P<pessoaId>[0-9]+)/$', views.visualizar, {'Classe': Avaliador}, name="pessoas_avaliadores_visualizar"),
    url(r'^avaliadores/excluir/(?P<pessoaId>[0-9]+)/$', views.excluir, {'Classe': Avaliador}, name="pessoas_avaliadores_excluir"),
]
