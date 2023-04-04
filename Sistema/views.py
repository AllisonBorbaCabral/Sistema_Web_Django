from django.views.generic import TemplateView

# Create your views here.


# def ConsultaPais(request, id):
#     return render(request, 'pais/pages/index.html', context={
#         'pais': pais.objects.get().getPais()
#     })


class Inicio(TemplateView):
    template_name = "Sistema/pages/index.html"
