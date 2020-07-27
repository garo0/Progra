# P1.a
def decimal(x):
    if x == "I":
        return 1
    elif x == "V":
        return 5
    elif x == "X":
        return 10
    elif x == "L":
        return 50
    elif x == "C":
        return 100
    elif x == "D":
        return 500
    elif x == "M":
        return 1000
    else:
        return 0


# P1.b
# decimal2: str str -> int
# devuelve el numero romano escrito como numero decimal
# ejemplo: decimal2("V","I") = 6
# ejemplo: decimal2("I","X") = 9
def decimal2(x, y):
    if x < y:
        return decimal(y) - decimal(x)
    elif decimal(x) == 0 or decimal(y) == 0:
        return 0
    else:
        return decimal(x) + decimal(y)


# P1.c
numRom = input("Ingres un numero romano de dos digitos: ")
x = numRom[0]
y = numRom[1]
print decimal2(x, y)

# P2.a
def primero(x):
    if x/10 == 0:
        return x
    return primero(x/10)


assert primero(5372) == 5
assert primero(5) == 5

# P2.b
def ultimos(x):
    largo = len(str(x))
    if largo == 1:
        return -1
    return x-primero(x)*10**(largo-1)


assert ultimos(5372) == 372
assert ultimos(5) == -1


# esCreciente: int -> bool
# La funcion devuelve un bool diciendo si sus digitos estan en orden creciente
# ejemplo: creciente(1224) = True
# ejemplo: creciente(2017) = False
def creciente(x):
    if len(str(x)) == 1:
        return True
    elif primero(x) <= primero(ultimos(x)):
        return creciente(ultimos(x))
    else:
        return False


assert creciente(1224) == True
assert creciente(2017) == False
