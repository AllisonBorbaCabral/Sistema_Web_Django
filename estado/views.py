from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from Sistema.Models.estado import estado

# Create your views here.


def EstadoIndex(request):
    estado_list = estado.objects.all()
    context = {'estado_list': estado_list}
    return render(request, 'estado/pages/ConsultaEstado.html', context)


class EstadoCreate(CreateView):
    model = estado
    fields = [
        'id', 'nm_estado', 'uf', 'pais'
    ]
    template_name = 'estado/pages/CadastroEstado.html'
    success_url = reverse_lazy('consulta-estado')
