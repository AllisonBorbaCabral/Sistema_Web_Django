from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from Sistema.Models.tamanho import tamanho

# Create your views here.


def TamanhoIndex(request):
    tamanho_list = tamanho.objects.all()
    context = {'tamanho_list': tamanho_list}
    return render(request, 'tamanho/pages/ConsultaTamanho.html', context)


class TamanhoCreate(CreateView):
    model = tamanho
    fields = [
        'id', 'ds_tamanho'
    ]
    template_name = 'tamanho/pages/CadastroTamanho.html'
    success_url = reverse_lazy('consulta-tamanho')
