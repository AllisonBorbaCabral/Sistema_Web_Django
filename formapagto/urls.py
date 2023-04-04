from django.urls import path

from . import views

urlpatterns = [
    path('formapagto/', views.FormaPagtoIndex, name='consulta-formapagto'),
    path('formapagto/cadastro/', views.FormaPagtoCreate.as_view(),
         name="cadastrar-formapagto"),
]
