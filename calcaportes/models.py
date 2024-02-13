from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

COMISIONES_AFAP = {
    'INTEGRA': 0.12,
    'SURACAP': 0.114,
    'UNIONCP': 0.12,
    'REPUBLI': 0.114,
}

class CalculoAportes(models.Model):

    AFAPUY_CHOICES = [
        ('INTEGRA', 'Integración AFAP'),
        ('SURACAP', 'Sura Capitales'),
        ('UNIONCP', 'Unión Capital'),
        ('REPUBLI', 'República AFAP'),
    ]

    fecha_con_zona_horaria = timezone.now()
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    # ahora, información a ingresar de los empleados
    nombre_empleado = models.CharField(max_length=50)
    apellido_empleado = models.CharField(max_length=50)
    salario_base = models.IntegerField()
    afap = models.CharField(max_length=7, choices=AFAPUY_CHOICES)
    fecha_ingreso = models.DateTimeField()
    diferencia_en_meses = models.IntegerField(blank=True, null=True)
    cantidad_de_hijos = models.IntegerField()

    class Meta:
        app_label = 'calcaportes'

    def __str__(self):
        return (f'{self.nombre_empleado} {self.apellido_empleado}')
    
    def save(self, *args, **kwargs):
        self.diferencia_en_meses = calcular_antiguedad_en_meses(self.fecha_ingreso)
        super().save(*args, **kwargs)

    def calcular_antiguedad_en_meses(fecha_ingreso):
        """
        Esta funcion calcula la diferencia en meses entre la fecha de ingreso y la fecha actual.
        Argumentos:
            fecha_ingreso: es la fecha de ingreso del empleado y lo recibe como paramtro.
        Retorno:
            angiguedad_en_meses: la diferencia en meses entre las dos fechas.
        """
        fecha_actual = datetime.now()
        diferencia_en_dias = (fecha_actual - fecha_ingreso).days
        antiguedad_en_meses = diferencia_en_dias // 30
        antiguedad_en_meses = None
        return antiguedad_en_meses

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
        # Una bonificación del 1% del sueldo base, por cada mes trabajado
        cantidad_meses_trabajados = 15
        #cantidad_meses_trabajados = calcular_antiguedad_en_meses()
        uno_porciento_del_salario_base = (self.salario_base)/100
        calculo_bonificacion = cantidad_meses_trabajados * uno_porciento_del_salario_base
        return calculo_bonificacion

    def asigna1(self):
        factor_asignacion = 0.05
        total_asignacion = (self.salario_base * factor_asignacion) * self.cantidad_de_hijos
        return total_asignacion

    def pago_fonasa1(self):
        pago_fonasa = self.salario_base * 0.07
        return pago_fonasa

    def pago_afap1(self):
        comision_afap = COMISIONES_AFAP[self.afap]
        return self.salario_base * comision_afap

    def base_imponible1(self):
        a = self.bonifica1()
        b = self.asigna1()
        base_impo = self.salario_base + a + b
        return base_impo
