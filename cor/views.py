from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from Sistema.Models.cor import cor

# Create your views here.


def CorIndex(request):
    cor_list = cor.objects.all()
    context = {'cor_list': cor_list}
    return render(request, 'cor/pages/ConsultaCor.html', context)


class CorCreate(CreateView):
    model = cor
    fields = [
        'id', 'ds_cor', 'situacao'
    ]
    template_name = 'cor/pages/CadastroCor.html'
    success_url = reverse_lazy('consulta-cor')
