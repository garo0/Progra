from funciones_tarea2 import *

print '-- Bienvenido al sistema de registro de contaminacion ambiental \n'
print '--- Ingrese listado de mediciones'
list = inputMedicion()
print ''
print '--- Numero de mediciones ingresadas:', cantidadMediciones(list)
print '--- Promedio:', promMediciones(list)
print '--- Min:', minMediciones(list)
print '---Max:', maxMediciones(list)
valorConsultado = float(raw_input('Ingrese un valor a consultar: '))
print '--- El valor ingresado pertenece al percentil:', percentilMedicion(valorConsultado, list)
emerAmbiental = float(raw_input('- Ingrese el valor para decretar emergencia ambiental: '))
print '--- Hubo', cantidadMayores(list, emerAmbiental), 'dias de emergencia ambiental'
