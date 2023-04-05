from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from Sistema.Models.pais import pais

# Create your views here.


def PaisIndex(request):
    pais_list = pais.objects.all()
    data = {'pais_list': pais_list}
    return render(request, 'pais/pages/ConsultaPais.html', data)


# render(request, 'pais/pages/ConsultaPais.html', context)


class PaisCreate(CreateView):
    model = pais
    fields = [
        'id', 'nm_pais', 'ddi', 'sigla'
    ]
    template_name = 'pais/pages/CadastroPais.html'
    success_url = reverse_lazy('consulta-pais')


# VIEW MODAL
def PaisView(request, pk):
    Pais = get_object_or_404(pais, pk=pk)
    data = {
        'funcao': 'PAÍS',
        'id': Pais.id,
        'nm_pais': Pais.nm_pais,
        'sigla': Pais.sigla,
        'cadastro': Pais.dt_cadastro,
        'alteracao': Pais.dt_ult_alt,
    }
    return JsonResponse(data)
