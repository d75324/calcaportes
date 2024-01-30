from django.shortcuts import render
from .models import CalculoAportes
from django.http import HttpRequest
from .forms import RegistroEmpleado


def home(request):
    return render(request, 'home.html')

def historico(request):
    return render(request, 'historico.html')

def registro(request):
    return render(request, 'registro.html')

class VistaFormularioHome(HttpRequest):
    def homeview(request):
        empleado = RegistroEmpleado()
        return render(request, 'home.html', {'form': empleado})

    def procesarhomeview(request):
        empleado = RegistroEmpleado()
        if empleado.is_valid():
            empleado.save()
            empleado = RegistroEmpleado() # instanciamos nuevamente para limpiar valores
            return render(request, 'home.html', {'form': empleado, 'message': 'Datos Procesados'})

