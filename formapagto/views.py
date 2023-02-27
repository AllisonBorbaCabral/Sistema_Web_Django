from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'formapagto/pages/cadastro.html', context={
        'name': 'Nome da Empresa'
    })
