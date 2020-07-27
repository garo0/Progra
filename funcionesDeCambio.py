from math import ceil
euro = 806.09
dolar = 718.55
yen = 6.71
libra = 861.74

# convertirMonedaAPesos: str num -> num
# convierte la moneda de origen en pesos
# ejemplo: convertirMonedaAPesos("dolares", 233) = 167422
# ejemplo: convertirMonedaAPesos("yenes", 345) = 2314
def convertirMonedaAPesos(moneda_origen, cantidad):
    if moneda_origen == "dolares":
        return int(dolar * cantidad)
    elif moneda_origen == "euros":
        return int(euro * cantidad)
    elif moneda_origen == "libras":
        return int(libra * cantidad)
    elif moneda_origen == "yenes":
        return int(yen * cantidad)
    else:
        return int(cantidad)


assert convertirMonedaAPesos("dolares", 233) == 167422
assert convertirMonedaAPesos("yenes", 345) == 2314

# convertirPesosAMoneda: num str -> num
# convierte pesos a la moneda de destino
# ejemplo: convertirPesosAMoneda(15608, "yenes") = 2326
# ejemplo: convertirPesosAMoneda(20384, "libras") = 23
def convertirPesosAMoneda(pesos, moneda_destino):
    if moneda_destino == "dolares":
        return int(pesos/dolar)
    elif moneda_destino == "euros":
        return int(pesos/euro)
    elif moneda_destino == "libras":
        return int(pesos/libra)
    elif moneda_destino == "yenes":
        return int(pesos/yen)
    else:
        return int(pesos)


assert convertirPesosAMoneda(15608, "yenes") == 2326
assert convertirPesosAMoneda(20384, "libras") == 23

# calcularComision: num num -> num
# calcula la comision respectiva al cambio
# ejemplo: calcularComision(12345.23, 0.2) = 2470
# ejemplo: calcularComision(32490, 0.3) = 9747
def calcularComision(pesos, comision):
    return int(ceil(pesos * comision))


assert calcularComision(12345.23, 0.2) == 2470
assert calcularComision(32490, 0.3) == 9747
