from django.urls import path

from . import views

urlpatterns = [
    path('cor/', views.CorIndex,
         name='consulta-cor'),
    path('cor/cadastro/', views.CorCreate.as_view(),
         name='cadastrar-cor'),
]
