from lista import *

# sumaLista: lista -> num
# suma una lista de tamanno arbitrario
# Ejemplos:
# sumaLista(crearLista(8,crearLista(72.4,listaVacia))) = 80.4
# sumaLista(crearLista(11,crearLista(5,crearLista(35,listaVacia)))) = 51
def sumaLista(L, suma=0):
    if L == None:
        return 0
    return cabeza(L) + sumaLista(cola(L))


listaA = crearLista(8,crearLista(72.4,listaVacia))
listaB = crearLista(11,crearLista(5,crearLista(35,listaVacia)))
listaC = listaVacia

assert sumaLista(listaA) == 80.4
assert sumaLista(listaB) == 51
assert sumaLista(listaC) == 0