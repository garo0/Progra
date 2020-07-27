from abstraccion import *
from fraccion import *

# menorQue: lista fraccion -> lista
# Devuelve una lista con todos los datos pertenecientes a la fraccion original que sean menores que la fraccion dada
# ej: menorQue(crearLista(fraccion(3,8), lista(fraccion(6,7), lista(fraccion(7,4), listaVacia))), fraccion(2,3)) = lista(fraccion(3,8), listaVacia)
def menorQue(L, frac):
    fracc = float(frac.numerador)/frac.denominador
    return filtro2(lambda x: float(x.numerador)/x.denominador < fracc, L)


# test
assert menorQue(crearLista(fraccion(3,8), lista(fraccion(6,7), lista(fraccion(7,4), listaVacia))), fraccion(2,3)) == lista(fraccion(3,8), listaVacia)

# inFrac: lista -> lista
# Invierte todas las fracciones de la lista dada
# ej: invFrac(crearLista(fraccion(3,8), lista(fraccion(6,7), lista(fraccion(7,4), listaVacia)))) = lista(fraccion(8,3), lista(fraccion(7,6), lista(fraccion(4,7), listaVacia)))
def invFrac(L):
    return mapa(lambda x: fraccion(x.denominador, x.numerador), L)


# test
assert invFrac(crearLista(fraccion(3,8), lista(fraccion(6,7), lista(fraccion(7,4), listaVacia)))) == lista(fraccion(8,3), lista(fraccion(7,6), lista(fraccion(4,7), listaVacia)))

# sumLista: lista -> fraccion
# Suma todas las fracciones de la lista dada
# ej: sumLista(crearLista(fraccion(3,8), lista(fraccion(6,7), lista(fraccion(7,4), listaVacia)))) = fraccion(668, 224)
def sumLista(L):
    return fold(lambda x, y: simplificaFracciones(sumaFracciones(x,y)), fraccion(0,1), L)


# test
assert sumLista(crearLista(fraccion(3,8), lista(fraccion(6,7), lista(fraccion(7,4), listaVacia)))) == fraccion(167, 56)
