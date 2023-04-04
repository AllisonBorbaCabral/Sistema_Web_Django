from django.urls import path

from . import views

urlpatterns = [
    path('cidade/', views.CidadeIndex, name='consulta-cidade'),
    path('cidade/cadastro/', views.CidadeCreate.as_view(), name="cadastrar-cidade"),
]
