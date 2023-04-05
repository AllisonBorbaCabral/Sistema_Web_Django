from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from Sistema.Models.cliente import cliente

# Create your views here.


def ClienteIndex(request):
    cliente_list = cliente.objects.all()
    context = {'cliente_list': cliente_list}
    return render(request, 'cliente/pages/ConsultaCliente.html', context)


class ClienteCreate(CreateView):
    model = cliente
    fields = [
        'id', 'nm_pessoa_razao_social', 'cpf_cnpj', 'rua', 'bairro', 'numero', 'complemento', 'cidade'
    ]
    template_name = 'cliente/pages/CadastroCliente.html'
    success_url = reverse_lazy('consulta-cliente')
