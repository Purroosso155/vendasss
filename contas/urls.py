from django.conf.urls import patterns,url
from models import ContaPagar, ContaReceber
from forms import FormContaPagar, FormContaReceber

urlpatterns = patterns('contas.views',
    url('^$', 'contas', name='contas'),
    url('^pagar/(?P<conta_id>\d+)/$', 'conta', {'classe': ContaPagar}, name='conta_a_pagar'),
    url('^receber/(?P<conta_id>\d+)/$', 'conta', {'classe': ContaReceber}, name='conta_a_receber'),
    url('^pagar/(?P<conta_id>\d+)/pagar/$', 'conta_pagamento', {'classe': ContaPagar}, name='conta_a_pagar_pagamento'),
    url('^receber/(?P<conta_id>\d+)/pagar/$', 'conta_pagamento', {'classe': ContaReceber}, name='conta_a_receber_pagamento'),
    url('^pagar/$', 'contas_por_classe', {'classe': ContaPagar, 'titulo': 'Contas a Pagar'}, name='contas_a_pagar'),
    url('^receber/$', 'contas_por_classe', {'classe': ContaReceber, 'titulo': 'Contas a Receber'}, name='contas_a_receber'),
    url('^pagar/nova/$', 'editar_conta',{'classe_form': FormContaPagar,'titulo': 'Conta a Pagar'},name='nova_conta_a_pagar'),
    url('^receber/nova/$', 'editar_conta',{'classe_form': FormContaReceber,'titulo': 'Conta a Receber'},name='nova_conta_a_receber'),
    url('^pagar/(?P<conta_id>\d+)/editar/$', 'editar_conta',{'classe_form': FormContaPagar,'titulo': 'Conta a Pagar'},name='editar_conta_a_pagar'),
    url('^receber/(?P<conta_id>\d+)/editar/$', 'editar_conta',{'classe_form': FormContaReceber,'titulo': 'Conta a Receber'},name='editar_conta_a_receber'),
    url('^pagar/(?P<conta_id>\d+)/excluir/$', 'excluir_conta',{'classe': ContaPagar,'proxima': '/contas/pagar/'},name='excluir_conta_a_pagar'),
    url('^receber/(?P<conta_id>\d+)/excluir/$', 'excluir_conta',{'classe': ContaReceber,'proxima': '/contas/receber/'},name='excluir_conta_a_receber'),


     )
