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
    salario_base = models.IntegerField()
    afap = models.CharField(max_length=7, choices=AFAPUY_CHOICES)
    fecha_ingreso = models.DateTimeField()
    cantidad_de_hijos = models.IntegerField()
    
    # ahora, los cálculos
    
    def __str__(self):
        return (f'{self.user_name}')

    def factores(self):
        bonifica = self.bonifica1()
        asigna = self.asigna1()
        pago_fonasa = self.pago_fonasa1()
        pago_afp = self.pago_afp1()
        base_imponible = self.base_imponible1()

    def bonifica1(self):
        # uso acá 15 meses como ejemplo pero lo tengo que calcular
        cantidad_meses_trabajados = 15
        factor0_bonifica1 = float(1+(cantidad_meses_trabajados/100))
        if self.salario_base is not None:
            self.salario_base = int(self.salario_base)
            return self.salario_base * factor0_bonifica1
        else:
            return 0  # salario_base no debería ser None, está definido como IntegerField
 
    def asigna1(self):
        factor_asignacion = 1.05
        if self.salario_base is not None:
            total_asignacion = self.salario_base * factor_asignacion * self.cantidad_de_hijos
            return total_asignacion
        else:
            return 0 # IDEM salario_base no debería ser None, está definido como IntegerField
        
    def pago_fonasa1(self):
        # no se como tomar los valores desde COMISIONES_AFAP
        # uso cualquier valor para el ejemplo
        if self.salario_base is not None:
            total_pago_fonasa = self.salario_base * 1.114
            return total_pago_fonasa
        else:
            return 0
'''
    def pago_afap1(self):
        # IDEM anterior, no se como tomar los valores desde COMISIONES_AFAP
        return self.salario_base * 0.114
    
    def base_imponible1(self):
        return self.salario_base + bonifica + asigna

'''    

bonifica = CalculoAportes()
bonifica.bonifica1()

asigna = CalculoAportes()
bonifica.asigna1()

pago_fonasa = CalculoAportes()
bonifica.pago_fonasa1()

#pago_afap = CalculoAportes()
#bonifica.pago_afap1()

'''
bonifica
asigna
pago_fonasa
pago_afp
base_imponible
'''