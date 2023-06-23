from django.http import HttpResponse

# Create your views here.

def index(request): # primera forma para establecer un view
    return HttpResponse("<h1>Bienvenidos a mi sitio de libros</h1>")