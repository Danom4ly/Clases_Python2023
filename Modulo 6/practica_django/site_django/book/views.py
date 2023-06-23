from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):  # primera forma para establecer un view
    return HttpResponse("<h1>Bienvenidos a mi sitio de libros</h1>")


class IndexPageView(TemplateView):
    template_name = 'index.html'
