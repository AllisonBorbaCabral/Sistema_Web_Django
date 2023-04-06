from django.urls import path

from . import views

urlpatterns = [
    path('pais/', views.PaisIndex, name='consulta-pais'),
    path('pais/cadastro/', views.PaisCreate, name="cadastrar-pais"),
    path('pais/editar/<int:pk>/', views.EditarPaisView.as_view(), name="editar-pais"),
    path("pais/<int:pk>/", views.PaisView, name="pais-view"),
]
