from django import forms
from .models import CalculoAportes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroEmpleado(forms.ModelForm):
    class Meta:
        model = CalculoAportes
        fields = [
            "nombre_empleado",
            "apellido_empleado",
            "salario_base",
            "afap",
            "fecha_ingreso",
            "cantidad_de_hijos"
        ]

class FormularioRegistroUsuarios(UserCreationForm):
    email_usuario = forms.EmailField(label="Correo Electronico Registro", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Un correo que revise regularmente'}))
    #nombre_usuario = forms.CharField(label="Nombre Usuario Registro", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Un nombre de Usuario, puede ser su nombre de pila'}))

    class Meta:
        model = User
        #fields = "__all__"
        fields = ('username', 'email_usuario', 'password1', 'password2')
    
        # FROM flatplanet
    def __init__(self, *args, **kwargs):
        super(FormularioRegistroUsuarios, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Ingrese un nombre de Usuario (Recomendado: su nombre de pila)'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Este campo es requerido. Puede usar hasta 30 caracteres, que pueden ser letras, dígitos y @, ., +, -, o _ unicamente.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ingrese una Password (no muy sencilla)'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Evite usar datos personales como passwords.</li><li>Su clave puede contener al menos 8 caracteres.</li><li>Evite usar passwords corrientes como usuario o admin.</li><li>Su password no puede ser enteramente numerica.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme la Password ingresada'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Re-ingrese su password a modo de verificacion.</small></span>'


