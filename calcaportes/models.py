from django.db import models

# Create your models here.

COMISIONES_AFAP = {
    'INTEGRA' : 1.12,
    'SURACAP' : 1.114,
    'UNIONCP' : 1.12,
    'REPUBLI' : 1.114,
}

class CalculoAportes(models.Model):
    
    AFAPUY_CHOICES = [
        ('INTEGRA', 'Integración AFAP'),
        ('SURACAP', 'Sura Capitales'),
        ('UNIONCP', 'Unión Capital'),
        ('REPUBLI', 'República AFAP'),
    ]
    
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    # ahora, información a ingresar de los empleados
    nombre_empleado = models.CharField(max_length=50)
    apellido_empleado = models.CharField(max_length=50)
    salario_base = models.FloatField()
    afap = models.CharField(max_length=7, choices=AFAPUY_CHOICES)
    fecha_ingreso = models.DateTimeField()
    cantidad_de_hijos = models.IntegerField()
    # ahora, los cálculos
    
    def __str__(self):
        return (f'{self.user_name}')

    def factores(self):
        calculo1 = self.bonificacion1()  
        calculo2 = self.bonificacion2()  
        calculo3 = self.bonificacion3()

    def bonificacion1(self):
        a = 2
        return self.afap * a
 
    def bonificacion2(self):
        b = 3
        return self.cantidad_de_hijos * b

    def bonificacion3(self):
        c = 115
        return self.salario_base * c/100

objeto_calculo = CalculoAportes()
objeto_calculo.bonificacion1()

'''
bonifica
asigna
pago_fonasa
pago_afp
base_imponible
'''