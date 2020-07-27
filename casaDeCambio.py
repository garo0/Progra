from funcionesDeCambio import *

pctj_comision = 0.2
assert 0 <= pctj_comision <= 1

print "Bienvenido a Beauchef Money eXchange!\n"+"sistema automatizado para realizar cambios de moneda\n"

input1 = raw_input("-Ingrese tipo de moneda que va a cambiar [pesos|dolares|euros|yenes|libras]: ")
input2 = input("--Ingrese monto en moneda " + input1 + ": ")
input3 = raw_input("-Ingrese tipo de moneda de destino [pesos|dolares|euros|yenes|libras]: ")

pesos = convertirMonedaAPesos(input1, input2)
comision = calcularComision(pesos, pctj_comision)
cambio = convertirPesosAMoneda((pesos-comision), input3)

print "\n-Ud. ha solicitado cambiar $"+str(input2), input1, "por", input3

if not ((input1 == "pesos" or input1 == "dolares" or input1 == "euros" or input1 == "yenes" or input1 == "libras") and
       (input3 == "pesos" or input3 == "dolares" or input3 == "euros" or input3 == "yenes" or input3 == "libras")):
    print "---- Moneda de origen ("+input1+") o destino ("+input3+") invalida\n"
elif cambio == 0:
    print "---- la cantidad", str(input2), "de", input1, "es insuficiente para cambiar a", input3 + "\n"
else:
    print "---esta transaccion tiene una comision de $"+str(comision), "pesos"
    print "----su cambio es:", str(cambio), input3+"\n"

print "Gracias por elegir Beauchef Money eXchange"
