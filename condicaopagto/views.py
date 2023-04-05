from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from Sistema.Models.condicaopagto import condicao_pagto

# Create your views here.


def CondicaoPagtoIndex(request):
    condicaopagto_list = condicao_pagto.objects.all()
    context = {'condicaopagto_list': condicaopagto_list}
    return render(request, 'condicaopagto/pages/ConsultaCondicaoPagto.html', context)


class CondicaoPagtoCreate(CreateView):
    model = condicao_pagto
    fields = [
        'id', 'ds_condicao_pagto', 'multa', 'juros', 'desc_financeiro'
    ]
    template_name = 'condicaopagto/pages/CadastroCondicaoPagto.html'
    success_url = reverse_lazy('consulta-condicaopagto')
