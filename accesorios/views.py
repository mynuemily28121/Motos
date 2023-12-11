from django.shortcuts import render
from .models import Accesorio

# Create your views here.
def accesorios(request):

    accesorios = Accesorio.objects.all()
    return render(request, "accesorios/accesorios.html", {"accesorios" : accesorios})