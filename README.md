## README ##

Una PyME, tiene la siguiente estructura de pagos para sus 10 empleados:

- Un sueldo base.
- Una bonificación del 1% del sueldo base, por cada mes trabajado.
- Una asignación familiar del 5% del sueldo base, por cada hijo.
- La suma de los tres valores anteriores, conforman la “base imponible”.

Todos los empleados están en FONASA, así que deben cotizar el 7% de la base imponible en salud. Los empleados están en una de dos AFAPs: AFP1 cobra (entre imposición y otros gastos) el 12 % de la base imponible, mientras que AFP2 cobra el 11.4%.

Construyan un programa Python que:

a) Pida el ingreso de datos de los 10 empleados y los almacene. Debe pedir: 1-Nombre 2-Apellido 3-Sueldo base 4-AFAP 5-Fecha de ingreso 6-Cantidad de hijos

b) El programa debe calcular la base imponible, según lo indicado arriba y luego descontar según corresponda.

c) El programa debe calcular lo que se debe pagar a FONASA y el monto de cada AFAP.

d) El programa debe calcular los promedios de pago a los empleados

e) El programa debe implementar control de excepciones en cada ingreso de información. El mensaje debe ser claro al usuario, indicando que debe corregir en cada intento de ingresar los datos.