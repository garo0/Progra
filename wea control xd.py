from lista import *

def juntar(L1,L2):
 if L1==None: return L2 #0.1
 return lista(cabeza(L1),juntar(cola(L1),L2))

L1 = lista(8,lista(32,None))
L2 = lista(43,lista(89,lista(54,None)))

print juntar(L1,L2)
