from lista import *


# inputMedicion: None -> lista
# Pide valores y los va ingresando a una lista hasta que se ingrese un '.'
# ejemplo:
# inputMedicion() = lista(valor=2.0, siguiente=lista(valor=1.0, siguiente=None)), donde el usuario
# introdujo los valores 1.0 y 2.0
def inputMedicion(list=listaVacia):
    num = raw_input('----- Ingrese medicion: ')
    if num != '.':
        return inputMedicion(list=crearLista(float(num), list))
    return list


# tests
if __name__ == "__main__":
    assert inputMedicion() == lista(valor=2.0, siguiente=lista(valor=1.0, siguiente=None))  # el usuario debe ingresar
    # 1.0, 2.0 y .


# cantidadMediciones: lista -> num
# Entrega la cantidad de mediciones contenidas en cierta lista
# ejemplo:
# cantidadMediciones(lista(valor=7.0, siguiente=lista(valor=6.0, siguiente=lista(valor=3.0, siguiente=None)))) = 3
def cantidadMediciones(list, cuantos=0):
    if type(list) == lista:
        return cantidadMediciones(cola(list), cuantos + 1)
    return cuantos


# test
assert cantidadMediciones(lista(valor=7.0, siguiente=lista(valor=6.0, siguiente=lista(valor=3.0, siguiente=None)))) == 3


# cantidadMayores: lista num -> num
# Entrega la cantidad de valores de la lista que son mayores que el valor ingresado
# ejemplo:
# cantidadMayores(lista(valor=2.0, siguiente=lista(valor=1.0, siguiente=None)),1) = 1
def cantidadMayores(list, valor, cant=0):
    if type(list) == lista:
        if valor <= cabeza(list):
            return cantidadMayores(cola(list), valor, cant + 1)
        return cantidadMayores(cola(list), valor, cant)
    return cant


# test
assert cantidadMayores(lista(valor=2.0, siguiente=lista(valor=1.0, siguiente=None)), 1) == 2


# percentilMedicion: num lista -> num
# Entrega el percentil al que pertenece el valor ingresado con respecto a la lista dada
# ejemplo:
# percentilMedicion(8, lista(valor=10.0, siguiente=lista(valor=9.0, siguiente=lista(valor=8.0,
# siguiente=lista(valor=7.0, siguiente=lista(valor=6.0, siguiente=lista(valor=5.0, siguiente=
# lista(valor=4.0, siguiente=lista(valor=3.0, siguiente=lista(valor=2.0, siguiente=lista(valor=1.0,
# siguiente=None)))))))))) = 70.0
def percentilMedicion(valor, list):
    pctj = (cantidadMediciones(list) - cantidadMayores(list, valor)) / float(cantidadMediciones(list))
    return round(pctj * 100)


# test
assert percentilMedicion(8, lista(valor=10.0, siguiente=lista(valor=9.0, siguiente=lista
(valor=8.0, siguiente=lista(valor=7.0, siguiente=lista(valor=6.0, siguiente=lista
(valor=5.0, siguiente=lista(valor=4.0, siguiente=lista(valor=3.0, siguiente=lista
(valor=2.0, siguiente=lista(valor=1.0, siguiente=None))))))))))) == 70.0


# maxMediciones: lista -> num
# Entrega el valor maximo de la lista dada
# ejemplo:
# maxMediciones(lista(valor=18.0, siguiente=lista(valor=33.0, siguiente=lista(valor=5.0, siguiente=None)))) = 33.0
def maxMediciones(list, maxi=True):
    if type(list) == lista:
        num = cabeza(list)
        if maxi == True:
            return maxMediciones(cola(list), maxi=num)
        if num > maxi:
            return maxMediciones(cola(list), maxi=num)
        return maxMediciones(cola(list), maxi)
    return maxi


# test
assert maxMediciones(lista(valor=18.0, siguiente=lista(valor=33.0, siguiente=lista(valor=5.0, siguiente=None)))) == 33.0


# minMediciones: lista -> num
# Entega el valor minimo de la lista dada
# ejemplo:
# minMediciones(lista(valor=18.0, siguiente=lista(valor=33.0, siguiente=lista(valor=5.0, siguiente=None)))) = 5.0
def minMediciones(list, mini=True):
    if type(list) == lista:
        num = cabeza(list)
        if mini == True:
            return minMediciones(cola(list), mini=num)
        if num < mini:
            return minMediciones(cola(list), mini=num)
        return minMediciones(cola(list), mini)
    return mini


# test
assert minMediciones(lista(valor=18.0, siguiente=lista(valor=33.0, siguiente=lista(valor=5.0, siguiente=None)))) == 5.0


# sumaLista: lista ->
# Entrega la suma de los valores de la lista
# ejemplo:
# sumaLista(lista(valor=18.5, siguiente=lista(valor=33.0, siguiente=lista(valor=5.5, siguiente=None)))) = 57
def sumaLista(list, suma=0):
    if type(list) == lista:
        return sumaLista(cola(list), suma + cabeza(list))
    return suma


# test
assert sumaLista(lista(valor=18.5, siguiente=lista(valor=33.0, siguiente=lista(valor=5.5, siguiente=None)))) == 57


# promMediciones: lista -> num
# Entrega el promedio entre los valores de la lista
# ejmplo:
# promMediciones(lista(valor=18.5, siguiente=lista(valor=33.0, siguiente=lista(valor=5.5, siguiente=None)))) = 19
def promMediciones(list):
    return sumaLista(list) / cantidadMediciones(list)


# test
assert promMediciones(lista(valor=18.5, siguiente=lista(valor=33.0, siguiente=lista(valor=5.5, siguiente=None)))) == 19
