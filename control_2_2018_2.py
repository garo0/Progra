# P1.a
from lista import *
import random

# eliminar: lista int -> lista
# recibe una lista y elimina el valor ubicado en la posicoon N
# ej: eliminar(lista(30,lista(40,lista(20,listaVacia))), 2) == lista(30,lista(20,listaVacia))
def eliminar(L, N):
    assert type(L) == lista and type(N) == int
    if N == 1:
        return cola(L)
    return lista(cabeza(L), eliminar(cola(L), N-1))

L = lista(30,lista(40,lista(20,listaVacia)))
assert eliminar(L,2) == lista(30,lista(20,listaVacia))

# P1.b

def tombola(L, K):
    if K == 0:
        return None
    n = random.randint(1,largoLista(L))
    valor = n_esimo(L, n)
    L1 = eliminar(L, n)
    return lista(valor, tombola(L1, K-1))


# P2.a

# lector: int arbol -> str
# lector de libro de codigo en bib
# ej: lector(10, bib) = '12345678-K'
def lector(cod, bib):
    if bib == None:
        return 'libro no existe'
    libro = bib.valor
    if cod < libro.codigo:
        return lector(cod, bib.izquierdo)
    elif cod > libro.codigo:
        return lector(cod, bib.derecho)
    elif lector.rutLector == '':
        return 'libro disponible'
    return libro.rutLector


# P2.b

