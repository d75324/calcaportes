from django.shortcuts import render, redirect
from .models import CalculoAportes
from .forms import RegistroEmpleado
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
    if request.method == "POST":
        # let's do a form:
        username = request.POST['user_name']
        password = request.POST['user_pass']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "El registro se procesó correctamente")
            return redirect('home')
        else:
            messages.success(request, "Por favor revisar los datos ingresados")
            return redirect('registro')
        
    else:
        return render(request, 'registro.html')

def login_user():
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'Salida Exitosa')
    return redirect('registro')