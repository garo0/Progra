import estructura

# Diseno de la estructura
# complejo: real (float) imaginario(int)
estructura.crear("complejo", "real imaginario")


# Contrato
# sumaComplejos: complejo complejo -> complejo

# Proposito
# crear un nuevo numero complejo que corresponda a la suma de dos numeros complejos c1 y c2

# Ejemplo:
# sumaComplejos(complejo(1,2), complejo(3,4))
# devuelve complejo(4,6)

# Cuerpo de la funcion
def sumaComplejos(c1, c2):
    real = c1.real + c2.real
    imaginario = c1.imaginario + c2.imaginario
    return complejo(real, imaginario)


# Test
c12 = complejo(1, 2)
c34 = complejo(3, 4)
assert sumaComplejos(c12, c34) == complejo(4, 6)


# multiplicacionComplejos: complejo complejo -> complejo
# Multiplica dos numeros complejos
# Ejemplo: multiplicacionComplejos(complejo(2,3),complejo(4,5)) = complejo(-7,22)
def multiplicacionComplejos(c1, c2):
    real = c1.real * c2.real - c1.imaginario * c2.imaginario
    imaginario = c1.real * c2.imaginario + c1.imaginario * c2.real
    return complejo(real, imaginario)


# Test
c23 = complejo(2, 3)
c45 = complejo(4, 5)
assert multiplicacionComplejos(c23, c45) == complejo(-7, 22)


# divisionComplejos: complejo complejo -> complejo
# Hace la division entre 2 numeros complejos
# ejemplos: divisionComplejos(complejo(3,2),complejo(1,-2)) = complejo(-1/5, 8/5)
def divisionComplejos(c1, c2):
    real = float(c1.real * c2.real + c1.imaginario * c2.imaginario) / (c2.real ** 2 + c2.imaginario ** 2)
    imaginario = float(c1.imaginario * c2.real - c1.real * c2.imaginario) / (c2.real ** 2 + c2.imaginario ** 2)
    return complejo(real, imaginario)


# Test
c32 = complejo(3,2)
c1_2 = complejo(1,-2)
assert divisionComplejos(c32, c1_2) == complejo(-1/5.0, 8/5.0)

