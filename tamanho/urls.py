from django.urls import path

from . import views

urlpatterns = [
    path('tamanho/', views.TamanhoIndex,
         name='consulta-tamanho'),
    path('tamanho/cadastro/', views.TamanhoCreate.as_view(),
         name='cadastrar-tamanho'),
]
