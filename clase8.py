import estructura

estructura.crear("fraccion", "numerador denominador")

a = fraccion(1,2)

print a.numerador
print a.denominador

def sumaFracciones(f1,f2):
    assert type(f1) == fraccion and type(f2) == fraccion
    assert f1.denominador != 0 and f2.denominador != 0

    num = f1.numerador*f2.denominador + f2.numerador*f1*denominador
    den = f1.denominador*f2.denominador

    return num/den


f12 = fraccion(1,2)
f34 = fraccion(3,4)

# assert sumaFracciones(f12, f34) == fraccion(10, 8)


def mcd(a,b):
    assert a !=0 and b !=0
    if a == b:
        return a
    mayor = max(a,b)
    menor = min(a,b)
    if mayor%menor==0:
        return menor
    else:
        return mcd(menor, mayor%menor)



def simplificaFracciones(f):
    mcd = mcd(f.numerador, f.denominador)
    num = f.numerador/mcd
    den = f.denominador/mcd

    return fraccion(num/den)

simplificaFracciones(fraccion(3,9))



