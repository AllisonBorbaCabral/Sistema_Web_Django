from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from Sistema.Models.pais import pais
from django.utils import timezone
from copy import copy


class CadastroPais(forms.Form):
    nm_pais = forms.CharField(label='* País', max_length=100)
    ddi = forms.CharField(label='* DDI', max_length=5)
    sigla = forms.CharField(label='* Sigla', max_length=3)


class CadastroPaisView(FormView):
    form_class = CadastroPais
    template_name = 'pais/pages/CadastroPais.html'
    success_url = reverse_lazy('consulta-pais')

    def form_valid(self, form):
        Pais = pais(nm_pais=form.cleaned_data['nm_pais'],
                    ddi=form.cleaned_data['ddi'], sigla=form.cleaned_data['sigla'])
        Pais.save()
        return super().form_valid(form)


class EditarPais(forms.ModelForm):
    class Meta:
        model = pais
        fields = ['id', 'nm_pais', 'ddi', 'sigla']


class EditarPaisView(UpdateView):
    model = pais
    form_class = EditarPais
    template_name = 'pais/pages/EditarPais.html'
    success_url = reverse_lazy('consulta-pais')

    def form_valid(self, form):
        # Armazenando os dados atuais em um objeto
        old_Pais = self.model.objects.get(pk=self.object.pk)
        Pais = form.save(commit=False)
        if Pais.nm_pais != old_Pais.nm_pais or Pais.ddi != old_Pais.ddi or Pais.sigla != old_Pais.sigla:
            Pais.dt_ult_alt = timezone.now()
        Pais.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['readonly_cadastro'] = self.object.readonly_cadastro
        context['readonly_alteracao'] = self.object.readonly_alteracao
        return context
