from django.urls import path

from . import views

urlpatterns = [
    path('pedido/', views.PedidoIndex, name='consulta-pedido'),
    path('pedido/cadastro/', views.PedidoCreate.as_view(), name='cadastrar-pedido'),
]
