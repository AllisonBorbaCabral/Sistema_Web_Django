from django import forms
from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic.edit import UpdateView

from Sistema.Models.pais import pais


class CadastroPais(forms.Form):
    nm_pais = forms.CharField(label='País', max_length=100)
    ddi = forms.CharField(label='DDI', max_length=5)
    sigla = forms.CharField(label='Sigla', max_length=3)
    dt_cadastro = forms.DateTimeField()
    dt_ult_alteracao = forms.DateTimeField()
    situacao = forms.CharField(label='Situação', max_length=1)


class EditarPaisView(UpdateView):
    model = pais
    template_name = 'pais/pages/EditarPais.html'
    success_url = reverse_lazy('consulta-pais')

    def form_valid(self, form):
        # Armazenando os dados atuais em um objeto
        old_Pais = self.model.objects.get(pk=self.object.pk)
        Pais = form.save(commit=False)
        if Pais.nm_pais != old_Pais.nm_pais or Pais.ddi != old_Pais.ddi or Pais.sigla != old_Pais.sigla:
            Pais.dt_ult_alt = datetime.now()
        Pais.save()
        return super().form_valid(form)
