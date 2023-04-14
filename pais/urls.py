# from django.urls import path

# from . import views

# urlpatterns = [
#     path('pais/', views.PaisIndex, name='consulta-pais'),
#     path('pais/cadastro/', views.PaisCreate, name="cadastrar-pais"),
#     path('pais/editar/<int:pk>/', views.PaisModalEdit, name="editar-pais"),
#     path('pais/atualizar/<int:pk>/', views.atualizar_pais, name="atualizar-pais"),

#     path("pais/<int:pk>/", views.PaisModalView, name="pais-view"),
# ]

from django.urls import path
from . import views

app_name = 'pais'

urlpatterns = [
    path('pais/', views.PaisListView.as_view(), name='lista-pais'),
    path('pais/cadastro/', views.PaisCreateView.as_view(), name="cadastrar-pais"),
    path('pais/consulta/<int:pk>/',
         views.PaisSelectView.modal_view, name="consulta-pais"),
    path('pais/editar/<int:pk>/',
         views.PaisUpdateView.modal_edit, name="editar-pais"),
    path('pais/excluir/<int:pk>/',
         views.PaisUpdateView.modal_edit, name="excluir-pais"),
]
