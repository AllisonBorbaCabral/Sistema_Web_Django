from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import *

from Sistema.Models.pais import pais

# Create your views here.


def PaisIndex(request):
    pais_list = pais.objects.all()
    data = {'pais_list': pais_list}
    return render(request, 'pais/pages/ConsultaPais.html', data)


def PaisCreate(request):
    return CadastroPaisView.as_view()(request)


def PaisEdit(request, pk):
    view = EditarPaisView.as_view()
    return view(request, pk)

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
