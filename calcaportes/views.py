from django.shortcuts import render
from .models import CalculoAportes
from .forms import RegistroEmpleado


def home(request):
    return render(request, 'home.html')

def historico(request):
    return render(request, 'historico.html')

def registro(request):
    return render(request, 'registro.html')
