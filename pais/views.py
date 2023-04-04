from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from Sistema.Models.pais import pais

# Create your views here.


def PaisIndex(request):
    pais_list = pais.objects.all()
    context = {'pais_list': pais_list}
    return render(request, 'pais/pages/ConsultaPais.html', context)


class PaisCreate(CreateView):
    model = pais
    fields = [
        'id', 'nm_pais', 'ddi', 'sigla'
    ]
    template_name = 'pais/pages/CadastroPais.html'
    success_url = reverse_lazy('consulta-pais')
