# P1.a
import random

def mover(casillaActual):
    dado = random.randint(2,12)
    if (casillaActual+dado)%9 == 0 and casillaActual < 63:
        return casillaActual+dado+9
    if casillaActual + dado > 63:
        return casillaActual
    else:
        return casillaActual+dado

def cantidadDeTurnos(casillaActual = 1, cantMov = 0):
    nuevaCasilla = mover(casillaActual)
    cantMovis = cantMov + 1
    if nuevaCasilla < 63:
        return cantidadDeTurnos(casillaActual=nuevaCasilla, cantMov=cantMovis)
    else:
        return cantMovis


print "cantidadDeTurnos:",cantidadDeTurnos()

# P2.a
# tengo esConjunto, pertenece, interseccion, union, resta, cardinal

def difSimetrica(x,y):
    if not(esConjunto(x) or esConjunto(y)):
        print "conjunto erroneo"
        return
    return resta(union(x,y), interseccion(x,y))


# P2.b
def pertenece(x, y):
    list1 = list()
    for i in range(0, len(str(y))):
        list1.append(str(y)[i])
    if str(x) in list1:
        return True
    else:
        return False



def interseccion(x, y, numero=str(0)):
    assert x >= 0
    divisor = len(str(x)) - 1
    primero = x / 10 ** divisor

    if x == 0:
        return int(numero)

    if pertenece(primero, y):
        numero = numero + str(primero)

    return interseccion(x - primero * 10 ** divisor, y, numero=numero)



print interseccion(312,436)
