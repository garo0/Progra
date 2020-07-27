# P1.a
# producto: int int -> int
# entrega el prodcuto entre x e y
# ejemplo: producto(6,9) = 54
#'''
def producto(x,y,res_main = 0):
    assert type(x) == int and type(y) == int and x>0 and y>0
    if y-1 == 0:
        return res_main + x
    else:
        res = res_main + x
        return producto(x,y-1,res_main = res)


assert producto(6,9) == 54
assert producto(5,2) == 10
#'''

# P1.b
# cuociente: int int -> num
# entrega el cuociente entre x e y
# ejemplo: cuociente(6,3) = 2
def cuociente(x, y, cuo=1):
    assert x > 0 and y > 0 and type(x) == int and type(y) == int
    if y == 1:
        return x
    elif x-y <= 0:
        return cuo
    else:
        return cuociente(x-y, y, cuo+1)

print cuociente(15,3)
assert cuociente(15,3) == 5

#'''
# P2.a

def f(x, n, suma=1):
    assert x != 0
    sumaPorAhora = suma + 1.0/(x**n)
    if n == 1:
        return sumaPorAhora
    else:
        return f(x, n-1, suma=sumaPorAhora)

x=input("x? ")

def converge(x,n=1):
    print "n=", n, "suma=", f(x, n)
    if n == 499:
        return "converge: no"
    elif (f(x,n+1) - f(x, n)) < 10**(-3):
        print "n=", n+1, "suma=", f(x, n+1)
        return "converge: si"
    else:
        m = n+1
        return converge(x, n = m)

print converge(x)



#'''


