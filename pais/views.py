
# from Sistema.Models.pais import pais

# # Create your views here.


# def PaisIndex(request):
#     pais_list = pais.objects.all()
#     data = {'pais_list': pais_list}
#     return render(request, 'pais/pages/ConsultaPais.html', data)


# def PaisCreate(request):
#     return CadastroPaisView.as_view()(request)

# # VIEW MODAL


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


from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, FormView, DetailView
from Sistema.Models.pais import pais
from .forms import *
import mysql.connector
from django.db import connection, transaction
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from django.http import JsonResponse
from django.template.loader import render_to_string


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
            'dt_cad': obj.dt_cadastro,
            'dt_ult': obj.dt_ult_alt
        }
        return JsonResponse(data)


class PaisCreateView(FormView):
    form_class = CadastroPais
    template_name = 'pais/pages/CadastroPais.html'
    success_url = reverse_lazy('consulta-pais')

    def form_valid(self, form):
        data = form.cleaned_data
        obj = {
            'nm_pais': data['nm_pais'],
            'ddi': data['ddi'],
            'sigla': data['sigla'],
            'dt_cadastro': timezone.now(),
            'dt_ult_alt': timezone.now(),
        }

        try:
            # Execução da query de insert
            with transaction.atomic():
                with connection.cursor() as cursor:
                    qy = "INSERT INTO sistema_pais (nm_pais, ddi, sigla, dt_cadastro, dt_ult_alteracao) VALUES (%s, %s, %s, %s, %s)"
                    values = (obj['nm_pais'], obj['ddi'], obj['sigla'],
                              obj['dt_cadastro'], obj['dt_ult_alt'])
                    cursor.execute(qy, values)
                    messages.success(
                        self.request, 'País cadastrado com sucesso.')

        except mysql.connector.Error as error:
            # Tratamento da exceção
            messages.error(
                self.request, f'Ocorreu um erro ao cadastrar o país: {error}')

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
