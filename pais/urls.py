from django.urls import path

from . import views

urlpatterns = [
    path('pais/', views.PaisIndex, name='consulta-pais'),
    path('pais/cadastro/', views.PaisCreate.as_view(), name="cadastrar-pais"),
]
