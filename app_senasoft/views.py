from django.shortcuts import render, redirect
from .models import Competidor
# Create your views here.

def bienvenida(request):
    return render(request, 'app_senasoft/bienvenida.html')

def registro(request):
    if request.method == 'POST':
        Competidor.objects.create(
            nombre=request.POST['nombre'],
            centro=request.POST['centro'],
            categoria=request.POST['categoria'],
        )
        return redirect('competidores')
    return render(request, 'app_senasoft/registro.html')

def competidores(request):
    lista = Competidor.objects.all()
    return render(request, 'app_senasoft/competidores.html', {'competidores': lista})