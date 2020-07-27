# mcd: int int -> int
# entrega el maximo comun divisor entres x e y
# ejemplo: mcd(18, 24) = 6

def mcd(x, y):
    assert type(x) == int and type(y) == int
    assert x >= 0 and y >= 0 and not (x == 0 and y == 0)
    if x == y or x == 0 or y == 0:
        return max(x, y)
    elif x > y:
        return mcd(x-y,y)
    else:
        return mcd(x,y-x)

# tests
assert mcd(18, 24) == 6
assert mcd(9, 4) == 1


assert mcd(19,32) == 1
