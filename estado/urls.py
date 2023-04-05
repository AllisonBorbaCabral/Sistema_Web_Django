from django.urls import path

from . import views

urlpatterns = [
    path('estado/', views.EstadoIndex, name='consulta-estado'),
    path('estado/cadastro/', views.EstadoCreate.as_view(), name="cadastrar-estado"),
    path("estado/<int:pk>/", views.EstadoView, name="estado-view"),
]
