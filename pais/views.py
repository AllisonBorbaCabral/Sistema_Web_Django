# def PaisIndex(request):
#     pais_list = pais.objects.all()
#     data = {'pais_list': pais_list}
#     return render(request, 'pais/pages/ConsultaPais.html', data)

# def PaisCreate(request):
#     return CadastroPaisView.as_view()(request)


# def PaisModalView(request, pk):
#     Pais = get_object_or_404(pais, pk=pk)
#     data = {
#         'funcao': 'PAÍS',
#         'id': Pais.id,
#         'nm_pais': Pais.nm_pais,
#         'sigla': Pais.sigla,
#         'cadastro': Pais.dt_cadastro,
#         'alteracao': Pais.dt_ult_alt,
#     }
#     return JsonResponse(data)


# # EDIT MODAL
# def PaisModalEdit(request, pk):
#     Pais = get_object_or_404(pais, pk=pk)
#     data = {
#         'funcao': 'EDITAR PAÍS',
#         'form': render_to_string('pais/pages/EditarPais.html', {'Pais': Pais})
#     }
#     return JsonResponse(data)


# @csrf_protect
# def atualizar_pais(request, pk):
#     Pais = get_object_or_404(pais, pk=pk)
#     if request.method == 'POST':
#         if (Pais.nm_pais != request.POST.get('nm_pais')) or (Pais.ddi != request.POST.get('ddi')) or (Pais.sigla != request.POST.get('sigla')):
#             Pais.dt_ult_alt = timezone.now()
#             Pais.nm_pais = request.POST.get('nm_pais')
#             Pais.ddi = request.POST.get('ddi')
#             Pais.sigla = request.POST.get('sigla')
#             Pais.save()
#             return redirect(reverse('consulta-pais'))
#     else:
#         return render(request, 'pais/pages/EditarPais.html', {'Pais': Pais})
from datetime import datetime

import mysql.connector
from django.contrib import messages
from django.db import connection, transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, FormView, ListView, UpdateView

# import logging

from Sistema.Models.pais import pais

from .forms import *


# import logging

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # Configuração do handler do logger
# log_file = 'logs/views.log'
# file_handler = logging.FileHandler(log_file)
# file_handler.setLevel(logging.INFO)
# file_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)


class PaisListView(ListView):
    model = pais
    template_name = 'pais/pages/ConsultaPais.html'
    context_object_name = 'pais_list'

    def get_queryset(self):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM sistema_pais')
            results = cursor.fetchall()
        return results


class PaisSelectView(DetailView):
    model = pais

    def modal_pais(request, pk):
        obj = get_object_or_404(pais, pk=pk)
        data = {
            'funcao': 'Detalhes',
            'id': obj.id,
            'nm_pais': obj.nm_pais,
            'sigla': obj.sigla,
            'ddi': obj.ddi,
            'dt_cad': obj.dt_cadastro.strftime('%d/%m/%Y - %H:%M:%S'),
            'dt_ult': obj.dt_ult_alteracao.strftime('%d/%m/%Y - %H:%M:%S')
        }
        return JsonResponse(data)


class PaisCreateView(FormView):
    form_class = CadastroPais
    template_name = 'pais/pages/CadastroPais.html'
    success_url = reverse_lazy('pais:lista-pais')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dt_cadastro'] = datetime.now()
        context['dt_ult_alteracao'] = datetime.now()

        return context

    def form_valid(self, form):
        print("CHEGUEI AQUI")
        data = form.cleaned_data
        teste = form.fields.values
        print(teste)

        obj = {
            'nm_pais': data['nm_pais'],
            'ddi': data['ddi'],
            'sigla': data['sigla'],
            'situacao': data['situacao'],
        }

        try:
            # Execução da query de insert
            with transaction.atomic():
                with connection.cursor() as cursor:
                    qy = "INSERT INTO sistema_pais (NM_PAIS, DDI, SIGLA, DT_CADASTRO, DT_ULT_ALTERACAO, SITUACAO) VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (obj['nm_pais'], obj['ddi'], obj['sigla'],
                              dt_cadastro, dt_ult_alteracao, obj['situacao'])
                    cursor.execute(qy, values)
                    messages.success(
                        self.request, 'País cadastrado com sucesso.')

                    # Log da execução bem-sucedida
                    # logger.info(f"Cadastro de país bem-sucedido: {obj}")

        except mysql.connector.Error as error:
            # Tratamento da exceção
            messages.error(
                self.request, f'Ocorreu um erro ao cadastrar o país: {error}')

            # Log do erro
            # logger.error(f"Erro ao cadastrar país: {error}")

        return super().form_valid(form)


# class PaisUpdateView(UpdateView):
#     model = pais
#     template_name = 'pais/pages/EditarPais.html'
#     form_class = CadastroPais
#     success_url = reverse_lazy('consulta-pais')

#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.dt_ult_alt = timezone.now()
#         obj.save()
#         return super().form_valid(form)
