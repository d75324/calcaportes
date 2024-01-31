from django.shortcuts import render
from .models import CalculoAportes
from .forms import RegistroEmpleado


def home(request):
    context = {}
    if request.method == 'POST':
        form_registro_empleado = RegistroEmpleado(request.POST)
        if form_registro_empleado.is_valid():
            registro_empleado_creado = form_registro_empleado.save()
            context['registro_empleado_creado'] = registro_empleado_creado
            # aportes = registro_empleado.calcular_aportes()
            form_registro_empleado = RegistroEmpleado()
    else:
        form_registro_empleado = RegistroEmpleado()
    context['form'] = form_registro_empleado
    return render(request, 'home.html', context)


def empleado(request, id):
    empleado = CalculoAportes.objects.get(id=id)
    context = {'empleado': empleado}
    return render(request, 'empleado.html', context)

def historico(request):
    context = {}
    empleados = CalculoAportes.objects.all()
    context['empleados'] = empleados
    return render(request, 'historico.html', context)

def registro(request):
    return render(request, 'registro.html')
