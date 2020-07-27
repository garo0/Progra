# areaCirculo: num -> num
# calcula el area de un circulo de radio r
# ejemplo: areaCirculo(2) = 12.56

def areaCirculo(r):
    pi=3.14
    return pi*r**2

assert areaCirculo(2) == 12.56

# areaAnillo: num num -> num
# calcula el area de un anillo
# radio interior, radio exterior
# ejemplo: areaAnillo(8,4) = 150.72

def areaAnillo(r_exterior, r_interior):
    return areaCirculo(r_exterior) - areaCirculo(r_interior)

assert areaAnillo(8,4) == 150.72

# perimetroCirculo: num -> num
# calcula el perimetro de un circulo de radio r
# ejemplo: perimetroCirculo(3) = 18.84

def perimetroCirculo(r):
    pi=3.14
    return 2*pi*r

assert perimetroCirculo(3) == 18.84

# perimetroAnillo: num num -> num
# calcula el perimetro de un anillo
# radio exterior, radio interior
# ejemplo: perimetroAnillo(7,3) = 62.8

def perimetroAnillo(r_exterior, r_interior):
    pi=3.14
    return perimetroCirculo(r_exterior) + perimetroCirculo(r_interior)

assert perimetroAnillo(7,3) == 62.8

