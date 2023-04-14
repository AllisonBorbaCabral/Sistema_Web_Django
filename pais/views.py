
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
from django.core.exceptions import ValidationError


from Sistema.Models.pais import pais

from .forms import CadastroPais, EditarPais


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

    def modal_view(request, pk):
        obj = get_object_or_404(pais, pk=pk)
        data = {
            'funcao': 'Detalhes',
            'id': obj.id,
            'nm_pais': obj.nm_pais,
            'sigla': obj.sigla,
            'ddi': obj.ddi,
            'dt_cad': obj.dt_cadastro.strftime('%d/%m/%Y - %H:%M:%S'),
            'dt_ult': obj.dt_ult_alteracao.strftime('%d/%m/%Y - %H:%M:%S'),
            'situacao': obj.situacao
        }
        return JsonResponse(data)


class PaisCreateView(FormView):
    form_class = CadastroPais
    template_name = 'pais/pages/CadastroPais.html'
    success_url = reverse_lazy('pais:lista-pais')

    def form_valid(self, form):
        data = form.cleaned_data
        obj = {
            'nm_pais': data['nm_pais'],
            'ddi': data['ddi'],
            'sigla': data['sigla'],
            'situacao': data['situacao'],
            'dt_cadastro': datetime.now(),
            'dt_ult_alteracao': datetime.now()
        }

        try:
            # Execução da query de insert
            with transaction.atomic():
                with connection.cursor() as cursor:
                    qy = "INSERT INTO sistema_pais (NM_PAIS, DDI, SIGLA, DT_CADASTRO, DT_ULT_ALTERACAO, SITUACAO) VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (obj['nm_pais'], obj['ddi'], obj['sigla'],
                              obj['dt_cadastro'], obj['dt_ult_alteracao'], obj['situacao'])
                    cursor.execute(qy, values)
                    messages.success(
                        self.request, 'País cadastrado com sucesso.')
        except mysql.connector.Error as error:
            # Tratamento da exceção
            messages.error(
                self.request, f'Ocorreu um erro ao cadastrar o país: {error}')
        return super().form_valid(form)

    def form_invalid(self, form):
        try:
            raise ValidationError('Algum erro ocorreu.')
        except ValidationError as e:
            messages.error(self.request, e)
            return self.render_to_response(self.get_context_data(form=form))


class PaisUpdateView(UpdateView):
    form_class = EditarPais
    model = pais
    template_name = 'pais/pages/EditarPais.html'
    success_url = reverse_lazy('pais:lista-pais')

    def modal_edit(request, pk):
        obj = get_object_or_404(pais, pk=pk)
        data = {
            'funcao': 'Editar',
            'id': obj.id,
            'nm_pais': obj.nm_pais,
            'sigla': obj.sigla,
            'ddi': obj.ddi,
            'dt_cad': obj.dt_cadastro.strftime('%d/%m/%Y - %H:%M:%S'),
            'dt_ult': obj.dt_ult_alteracao.strftime('%d/%m/%Y - %H:%M:%S'),
            'situacao': obj.situacao
        }
        return JsonResponse(data)

    # def form_valid(self, form):
    #     Pais = get_object_or_404(pais, pk=self.object.pk)
    #     data = form.cleaned_data
    #     obj = {
    #         'id': data['id'],
    #         'nm_pais': data['nm_pais'],
    #         'ddi': data['ddi'],
    #         'sigla': data['sigla'],
    #         'situacao': data['situacao'],
    #         'dt_ult_alteracao': datetime.now()
    #     }

    #     try:
    #         # Execução da query de update
    #         with transaction.atomic():
    #             with connection.cursor() as cursor:
    #                 if obj['nm_pais'] != Pais.nm_pais or obj['ddi'] != Pais.ddi or obj['sigla'] != Pais.sigla or obj['situacao'] != Pais.situacao:
    #                     qy = "UPDATE sistema_pais SET NM_PAIS = %s, DDI = %s, SIGLA = %s, situacao = %s, DT_ULT_ALTERACAO = %s WHERE ID = %s"
    #                     values = (obj['nm_pais'], obj['ddi'], obj['sigla'],
    #                               obj['situacao'], datetime.now(), obj['id'])
    #                     cursor.execute(qy, values)
    #                     messages.success(
    #                         self.request, 'País cadastrado com sucesso.')
    #     except mysql.connector.Error as error:
    #         # Tratamento da exceção
    #         messages.error(
    #             self.request, f'Ocorreu um erro ao cadastrar o país: {error}')
    #     return super().form_valid(form)
