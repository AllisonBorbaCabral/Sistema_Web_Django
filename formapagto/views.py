from django.shortcuts import render

from Sistema.models import pais

# Create your views here.


def home(request):
    return render(request, 'formapagto/pages/cadastro.html', context={
        'name': pais.objects.get().Pais()
    })
