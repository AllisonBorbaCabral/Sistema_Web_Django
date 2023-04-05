from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from Sistema.Models.pedido import pedido

# Create your views here.


def PedidoIndex(request):
    pedido_list = pedido.objects.all()
    context = {'pedido_list': pedido_list}
    return render(request, 'pedido/pages/ConsultaPedido.html', context)


class PedidoCreate(CreateView):
    model = pedido
    fields = [
        'id', 'cliente'
    ]
    template_name = 'pedido/pages/CadastroPedido.html'
    success_url = reverse_lazy('consulta-pedido')
