import math

# perimetro: num num num -> num
# calcula el perimetro de un triangulo de lados a, b, c
# ejemplo: perimetro(2,3,2) debe dar 7

def perimetro(a, b, c):
  return a+b+c
# Tests
assert perimetro(2,3,2) == 7

# area: num num num -> num
# calcula el area de un triangulo de lados a, b, c
# ejemplo: area(3,  4, 5) debe dar 6

def area(a, b, c):
  semi_perimetro = perimetro(a,b,c)/2
  return math.sqrt(semi_perimetro*(semi_perimetro-a)*(semi_perimetro-b)*(semi_perimetro-c))
# Tests
assert area(3,4,5) == 6
