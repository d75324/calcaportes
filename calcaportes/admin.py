from django.contrib import admin
from .models import CalculoAportes

# Register your models here.

class DataBackEnd(admin.ModelAdmin):
    list_display = (
                    'created_at',
                    'user_name',
                    'user_email',
                    'nombre_empleado',
                    'apellido_empleado',
                    'salario_base',
                    'afap',
                    'fecha_ingreso',
                    'cantidad_de_hijos',
                   )
    search_fields = (
                    'created_at',
                    'user_name',
                    'user_email',
                    'nombre_empleado',
                    'apellido_empleado',
                    'afap',
                    'fecha_ingreso',
                    )
    list_filter = (
                    'created_at',
                    'user_name',
                    'user_email',
                    'nombre_empleado',
                    'apellido_empleado',
                    'afap',
                    'fecha_ingreso',
                  )
    
admin.site.register(CalculoAportes, DataBackEnd)