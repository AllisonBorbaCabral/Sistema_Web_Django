from django.urls import path

from formapagto.views import home

urlpatterns = [
    path('teste/', home),
]
