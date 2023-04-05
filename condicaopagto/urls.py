from django.urls import path

from . import views

urlpatterns = [
    path('condicaopagto/', views.CondicaoPagtoIndex,
         name='consulta-condicaopagto'),
    path('condicaopagto/cadastro/', views.CondicaoPagtoCreate.as_view(),
         name='cadastrar-condicaopagto'),
]
