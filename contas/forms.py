from django import forms
from models import ContaPagar, ContaReceber
from django.forms.extras.widgets import SelectDateWidget


class FormPagamento(forms.Form):
    valor = forms.DecimalField(max_digits=15,decimal_places=2)
    data = forms.DateField()
    def salvar_pagamento(self, conta):
        return conta.lancar_pagamento(
            data_pagamento=self.cleaned_data['data'],
            valor=self.cleaned_data['valor'],
        )

class FormContaPagar(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.base_fields[
            'data_vencimento'
        ].widget = SelectDateWidget()
        self.base_fields[
            'data_pagamento'
        ].widget = SelectDateWidget()
        super(FormContaPagar, self).__init__(*args, **kwargs)
    class Meta:
        model = ContaPagar
        exclude = ('usuario','operacao')


class FormContaReceber(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.base_fields[
            'data_vencimento'
        ].widget = SelectDateWidget()
        self.base_fields[
            'data_pagamento'
        ].widget = SelectDateWidget()
        super(FormContaReceber, self).__init__(*args, **kwargs)
    class Meta:
        model = ContaReceber
        exclude = ('usuario','operacao')