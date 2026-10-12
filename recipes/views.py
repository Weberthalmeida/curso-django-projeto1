from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context = {'name': 'Weberth de Almeida'})
