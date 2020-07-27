import triangulo

print 'Calcular el area y perimetro de un triangulo' 
l1 = input('Ingrese el largo del primer lado ')
l2 = input('Ingrese el largo del segundo lado ')
l3 = input('Ingrese el largo del tercer lado ')

print 'El perimetro del triangulo es ', triangulo.perimetro(l1, l2, l3) 
print 'El area del triangulo es ', triangulo.area(l1, l2, l3)
