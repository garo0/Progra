import estructura
# Diseno de la estructura
# fraccion: numerador (int) denominador(int)
estructura.crear("fraccion", "numerador denominador")

# Contrato
# sumaFracciones: fraccion fraccion -> fraccion

# Proposito
# crear una nuva fraccion que corresponda a la suma de dos fracciones f1 y f2

# Ejemplo:
# sumaFracciones(fraccion(1,2), fraccion(3,4))
# devuelve fraccion(10,8)

# Plantilla
# def funcionConFracciones(fraccion1, fraccion2):
# 	... fraccion1.numerador ... fraccion2.numerador ...
# 	... fraccion1.numerador ... fraccion2.denominador ...
# 	... fraccion1.denominador ... fraccion2.numerador ...
# 	... fraccion1.denominador ... fraccion2.denominador ...

# Cuerpo de la funcion
def sumaFracciones(f1,f2):
  assert type(f1) == fraccion and type(f2)==fraccion
  assert f1.denominador != 0 and f2.denominador != 0
  num = f1.numerador*f2.denominador \
        + f1.denominador*f2.numerador
  den = f1.denominador*f2.denominador
  return fraccion(num,den)
  
# Test
f12=fraccion(1,2)
f34=fraccion(3,4)
assert sumaFracciones(f12,f34) == fraccion(10,8)





def pruebaSuma():
  print "suma de fracciones a/b y c/d"
  a=input("a?")
  b=input("b?")
  f1=fraccion(a,b)
  f2=fraccion(input("c?"),input("d?"))
  f3=sumaFracciones(f1,f2)
  print "suma=" + str(f3.numerador) + "/" + str(f3.denominador)



def aString(f):
  return str(f.numerador)+"/"+str(f.denominador)

assert aString(fraccion(1,2)) == "1/2"



# Contrato
# restaFracciones: fraccion fraccion -> bool

# Proposito
# Indica si las fracciones f1 y f2 son equivalentes

# Ejemplo:
# restaFracciones(fraccion(1,2), fraccion(3,6))
# devuelve fraccion(-2,8)

# Plantilla
# def funcionConFracciones(fraccion1, fraccion2):
# 	... fraccion1.numerador ... fraccion2.numerador ...
# 	... fraccion1.numerador ... fraccion2.denominador ...
# 	... fraccion1.denominador ... fraccion2.numerador ...
# 	... fraccion1.denominador ... fraccion2.denominador ...

# Cuerpo de la funcion
def restaFracciones(f1,f2):
  assert type(f1) == fraccion and type(f2)==fraccion
  assert f1.denominador != 0 and f2.denominador != 0
  num = f1.numerador*f2.denominador \
        - f1.denominador*f2.numerador
  den = f1.denominador*f2.denominador
  return fraccion(num,den)
  
# Test
f12=fraccion(1,2)
f34=fraccion(3,4)
assert restaFracciones(f12,f34) == fraccion(-2,8)

# Contrato
# mcd: int int -> int

# Proposito
# encuentra el maximo comun divisor para dos numeros

# Ejemplo:
# mcd(12, 18) -> 6

# Cuerpo de la funcion
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
  
  
# Test
assert mcd(18,12)==6



# Contrato
# simplificaFracciones: fraccion -> fraccion

# Proposito
# entrega una fraccion nueva que es la version simplificada de f

# Ejemplo:
# simplificaFracciones(fraccion(10,30)) -> fraccion(1,3)

# Plantilla
# def simplificaFracciones(fraccion):
# 	... fraccion.numerador ... fraccion.denominador

# Cuerpo de la funcion
def simplificaFracciones(f):
  m = mcd(f.numerador,f.denominador)
  return fraccion(f.numerador/m,f.denominador/m)  

# Test
assert simplificaFracciones(fraccion(10,30)) == fraccion(1,3)





# Contrato
# equivalenciaFracciones: fraccion fraccion -> bool

# Proposito
# Indica si las fracciones f1 y f2 son equivalentes

# Ejemplo:
# equivalenciaFracciones(fraccion(1,2), fraccion(3,6))
# devuelve True

# Plantilla
# def funcionConFracciones(fraccion1, fraccion2):
# 	... fraccion1.numerador ... fraccion2.numerador ...
# 	... fraccion1.numerador ... fraccion2.denominador ...
# 	... fraccion1.denominador ... fraccion2.numerador ...
# 	... fraccion1.denominador ... fraccion2.denominador ...

# Cuerpo de la funcion
def igualdadFracciones(f1,f2):
  return simplificaFracciones(f1)==simplificaFracciones(f2)  

# Test
f12=fraccion(1,2)
f36=fraccion(3,6)
assert igualdadFracciones(f12,f36)
