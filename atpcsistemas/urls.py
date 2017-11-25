from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'meusite.views.android_intro', ),
                       url(r'^atpcsistemas/', include('meusite.urls')),

    (r'^contato/$', 'atpcsistemas.views.contato'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contas/', include('contas.urls')),
    url(r'^SalesSystem/', include('SalesSystem.urls')),
                       url(r'^salesystem/', include('SalesSystem.urls')),
                       url(r'^salessistem/', include('SalesSystem.urls')),
                       url(r'^salesistem/', include('SalesSystem.urls')),
                       url(r'^josias/', include('SalesSystem.urls')),
                       url(r'^salessystem/', include('SalesSystem.urls')),
    url(r'^entrar/$', 'django.contrib.auth.views.login',
    {'template_name': 'entrar.html'}, 'entrar'),
    url(r'^login/$', 'django.contrib.auth.views.login',
    {'template_name': 'login.html'}, 'entrar'),
    url(r'^sair/$', 'django.contrib.auth.views.logout',
    {'template_name': 'python_intro.html'}, 'sair'),
    url(r'^cadastrar/$', 'atpcsistemas.views.cadastrar', {}, 'cadastrar'),
    url(r'^home/$', 'SalesSystem.views.home', {},),
    url(r'^$', 'meusite.views.python_intro',),
    url(r'^bemvindo/$', 'atpcsistemas.views.bemvindo', {}, 'bem_vindo.html'),
    url(r'^mensagem/$', 'atpcsistemas.views.mensagem', {}, 'mensagem.html'),
    url(r'^contatoenviado/$', 'atpcsistemas.views.contatoenviado', {}, 'contatoenviado.html'),
                       )








if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                    {'document_root': settings.MEDIA_ROOT}),
                            )



