# -*- coding: utf-8 -*-
from saludoFunciones import *

# saludo: int(perteneciente a  [1 y 24]) -> str
# Determinar el saludo adecuado a la hora del dia 1 <= h <= 24
# ejemplos:
# saludo(11) debe devolver Buenos dias!
# saludo(15) debe devolver Buenas tardes!

def saludo(hora):
    ## condiciones
    if esDia(hora) == True:
        return "Buenos dias!"
    elif esTarde(hora) == True:
        return "Buenas tardes!"
    else:
        return "Buenas noches!"

# test:
assert saludo(1) == 'Buenos dias!'
assert saludo(11) == 'Buenos dias!'
assert saludo(12) == 'Buenas tardes!'
assert saludo(15) == 'Buenas tardes!'
assert saludo(21) == 'Buenas noches!'
assert saludo(23) == 'Buenas noches!'
assert saludo(24) == 'Buenas noches!'