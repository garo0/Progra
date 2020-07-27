# encoding: utf-8

import random
from lista import *
import estructura

# Funciones de la clase

#Arbol Binario
#AB: valor(any), izq(AB), der(AB)
estructura.crear("AB","valor izq der")


def buscaValor(x, arbol):
    assert arbol == None or type(arbol) == AB
    if arbol == None:
        return False

    elif arbol.valor == x:
        return True
    elif x < arbol.valor:
        return buscaValor(x, arbol.izq)
    elif x > arbol.valor:
        return buscaValor(x, arbol.der)


def escribir(arbol):
    assert arbol == None or type(arbol) == AB
    if arbol == None:
        return

    escribir(arbol.izq)
    print arbol.valor
    escribir(arbol.der)


def insertar(x, arbol):
    assert arbol == None or type(arbol) == AB
    if arbol == None:
        return AB(x, None, None)

    assert x != arbol.valor
    if x < arbol.valor:
        return AB(arbol.valor, insertar(x, arbol.izq), arbol.der)
    if x > arbol.valor:
        return AB(arbol.valor, arbol.izq, insertar(x, arbol.der))


# Funciones creadas por mi

# generadorLista100: None -> lista
# Entrega una lista con 100 numeros al azar entre 1 y 9999
def generadorLista100(L=listaVacia, n=0):
    if n == 100:
        return L
    random_num = random.randint(1,9999)
    L = lista(random_num, L)
    return generadorLista100(L, n+1)

# ordenar: lista -> None
# Ordena los valores de una lista en orden creciente con un ABB
def ordenar(L, ABB = True):
    if vacia(L):
        return escribir(ABB)

    elif ABB == True:
        ABB = AB(cabeza(L), None, None)
        return ordenar(cola(L), ABB)

    elif not buscaValor(cabeza(L), ABB):
        ABB = insertar(cabeza(L), ABB)
        return ordenar(cola(L), ABB)

    return ordenar(cola(L), ABB)


# Ejemplo con lista de 100 numeros
ordenar(generadorLista100())