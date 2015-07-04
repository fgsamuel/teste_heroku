# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

from fisioProject import settings

import views as fisio_view


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', fisio_view.index, name="home"),

    url(r'^pessoas/', include('pessoas.urls')),
    
    url(r'^avaliacoes/', include('avaliacoes.urls')),
    
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
