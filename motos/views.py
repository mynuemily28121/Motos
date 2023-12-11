from django.shortcuts import render
from motos.models import Moto

# Create your views here.
def motos(request):
    
    motos = Moto.objects.all()
    return render(request, "motos/motos.html", {"motos":motos})