T=[["gabriela",62,45],\
   ["jose",48,52],\
   ["rosa",56,35],\
   ["matias",49,48]]

# Entrega promedio de una pregunta a base de una lista y el numero de la pregunta
def promP(T,x):
    sumP = 0
    for i in T:
        sumP += i[x]
    P = float(sumP)/len(T)
    return P


# Entrega promedio de las pregunta del alumno en base a una lista y el numero del alumno
def promA(T, x):
    sumA = 0
    for i in range(1,len(T[x])):
        sumA += T[x][i]
    A = float(sumA) / (len(T[x])-1)
    return A


print 'Promedios por pregunta'
for i in range(1,len(T[0])):
    print 'Promedio pregunta', str(i), ':', str(promP(T, i))

print '\nPromedios por alumno'
for i in range(len(T)):
    print 'Alumno:', T[i][0]
    print 'Promedio:', str(promA(T, i))
