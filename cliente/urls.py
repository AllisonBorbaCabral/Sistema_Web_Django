from django.urls import path

from . import views

urlpatterns = [
    path('cliente/', views.ClienteIndex, name='consulta-cliente'),
    path('cliente/cadastro/', views.ClienteCreate.as_view(),
         name="cadastrar-cliente"),
]
