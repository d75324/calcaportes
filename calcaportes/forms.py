from django import forms
from .models import CalculoAportes


class RegistroEmpleado(forms.ModelForm):
    class Meta:
        model = CalculoAportes
        fields = [ "nombre_empleado",
                    "apellido_empleado",
                    "salario_base",
                    "afap",
                    "fecha_ingreso",
                    "cantidad_de_hijos"
                 ]
        
        