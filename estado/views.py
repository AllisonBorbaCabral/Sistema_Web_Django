from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
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


# VIEW MODAL
def EstadoView(request, pk):
    Estado = get_object_or_404(estado, pk=pk)
    data = {
        'funcao': 'ESTADO',
        'id': Estado.id,
        'nm_estado': Estado.nm_estado,
        'uf': Estado.uf,
        'cadastro': Estado.dt_cadastro,
        'alteracao': Estado.dt_ult_alt,
    }
    return JsonResponse(data)
