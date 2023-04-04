from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from Sistema.Models.cidade import cidade

# Create your views here.


def CidadeIndex(request):
    cidade_list = cidade.objects.all()
    context = {'cidade_list': cidade_list}
    return render(request, 'cidade/pages/ConsultaCidade.html', context)


class CidadeCreate(CreateView):
    model = cidade
    fields = [
        'id', 'nm_cidade', 'ddd', 'estado'
    ]
    template_name = 'cidade/pages/CadastroCidade.html'
    success_url = reverse_lazy('consulta-cidade')
