from django.db import models

# Create your models here.

COMISIONES_AFAP = {
    'INTEGRA': 1.12,
    'SURACAP': 1.114,
    'UNIONCP': 1.12,
    'REPUBLI': 1.114,
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
    salario_base = models.IntegerField()
    afap = models.CharField(max_length=7, choices=AFAPUY_CHOICES)
    fecha_ingreso = models.DateTimeField()
    cantidad_de_hijos = models.IntegerField()

    class Meta:
        app_label = 'calcaportes'

    def __str__(self):
        return (f'{self.nombre_empleado}')

    def calcular_aportes(self):
        bonifica = self.bonifica1()
        asigna = self.asigna1()
        pago_fonasa = self.pago_fonasa1()
        pago_afp = self.pago_afap1()
        base_imponible = self.base_imponible1()
        aportes_totales = bonifica + asigna + pago_fonasa + pago_afp + base_imponible
        return aportes_totales
    
    def bonifica1(self):
        # uso acá 15 meses como ejemplo pero ## LO TENGO QUE CALCULAR ##
        cantidad_meses_trabajados = 15
        factor = float(1+(cantidad_meses_trabajados/100))
        return self.salario_base * factor

    def asigna1(self):
        factor_asignacion = 1.05
        total_asignacion = self.salario_base * factor_asignacion * self.cantidad_de_hijos
        return total_asignacion

    def pago_fonasa1(self):
        total_pago_fonasa = self.salario_base * 1.114
        return total_pago_fonasa

    def pago_afap1(self):
        comision_afap = COMISIONES_AFAP[self.afap]
        return self.salario_base * comision_afap

    def base_imponible1(self):
        return self.salario_base

# '''
# # ESTAS SON LAS COSAS QUE TENGO QUE CALCULAR # #
# bonifica
# asigna
# pago_fonasa
# pago_afp
# base_imponible
# '''

# ca1 = CalculoAportes(
#     user_name='juan',
#     user_email='juan@example.com',
#     nombre_empleado='juan',
#     apellido_empleado='perez',
#     salario_base=1000,
#     afap='INTEGRA',
#     fecha_ingreso='2020-01-01T00:00:00Z',
#     cantidad_de_hijos=2
# )
# ca1.save()

# ca2 = CalculoAportes(
#     user_name='juan2',
#     user_email='juan2@example.com',
#     nombre_empleado='juan2',
#     apellido_empleado='perez',
#     salario_base=1000,
#     afap='SURACAP',
#     fecha_ingreso='2020-01-01T00:00:00Z',
#     cantidad_de_hijos=3
# )
# ca2.save()
