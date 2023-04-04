from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from Sistema.Models.formapagto import forma_pagto

# Create your views here.


def FormaPagtoIndex(request):
    formapagto_list = forma_pagto.objects.all()
    context = {'formapagto_list': formapagto_list}
    return render(request, 'formapagto/pages/ConsultaFormaPagto.html', context)


class FormaPagtoCreate(CreateView):
    model = forma_pagto
    fields = [
        'id', 'ds_forma_pagto', 'situacao'
    ]
    template_name = 'formapagto/pages/CadastroFormaPagto.html'
    success_url = reverse_lazy('consulta-formapagto')
