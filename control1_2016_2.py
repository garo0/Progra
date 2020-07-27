# P1.a)
def sumaProductos(x,y, suma = 0):
    if x == 0 or y == 0:
        return suma
    else:
        return sumaProductos(x/10,y/10,suma+(x%10)*(y%10))

assert sumaProductos(372,4332) == 34
assert sumaProductos(12345,6789) == 110


# P1.b)
def RUN(x):
    n = sumaProductos(x, 32765432)
    d = 11-(n%11)
    if d == (10 or 11):
        return "K"
    else:
        return d


# P1.c)
run = input("Inserte su RUN (sin digito verificador): ")
print "Su RUN es:",str(run)+"-"+str(RUN(run))

