from django.shortcuts import render, redirect
from .models import CalculoAportes
from .forms import RegistroEmpleado
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
import csv

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
    empleados = CalculoAportes.objects.all().order_by('-created_at')
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


def logout_user(request):
    logout(request)
    messages.success(request, 'Salida Exitosa')
    return redirect('registro')

def exportar_a_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="aportes.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre y Apellido',
                    'Salario Base',
                    'Bonificación',
                    'Asignación',
                    'Base Imponible',
                    'Pago AFAP',
                    'Pago Fonasa'])  # Encabezados de columna

    # Traigo los datos del modelo y los itero
    datos = CalculoAportes.objects.all()

    for dato_for in datos:
        nombre_completo = f"{dato_for.nombre_empleado} {dato_for.apellido_empleado}"
        writer.writerow([nombre_completo,
                        round(dato_for.salario_base, 2),
                        round(dato_for.bonifica1(), 2),
                        round(dato_for.asigna1(), 2),
                        round(dato_for.base_imponible1(), 2),
                        round(dato_for.pago_afap1(), 2),
                        round(dato_for.pago_fonasa1(), 2)])  # Datos que van a ir en cada fila

    return response
