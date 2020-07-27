# -*- coding: utf-8 -*-

# tiendita.py 
## para completar
## no se pueden modificar los parametros de las funciones


import estructura
estructura.mutable("producto","nombre precio cantidad")

productos = []

# crearInventario: None -> None
# efecto: pide al usuario agregar datos de productos para
# guardarlos en el inventario de la tienda (variable global 'inventario'). 
# No permite agregar productos repetidos ni que el precio y/o el stock sea menor que 1.
def crearInventario():
    print('- CREANDO INVENTARIO DE TIENDA -\n'+'- AGREGUE PRODUCTOS PARA VENDER -\n')
    SoN = raw_input('agregar nuevo producto[s/n]: ')
    while SoN == 's':
        prod = raw_input('- nombre producto? ')
        if prod in productos:
            print '--- el producto ya existe!'
        else:
            cant = int(raw_input('- cantidad en stock? '))
            if cant < 1:
                print 'La cantidad ingresada no es valida'
            else:
                prec = int(raw_input('- precio unitario? '))
                if prec < 1:
                    print 'El precio ingresado no es valido'
                else:
                    print '--- producto agregado:', prod, 'precio= $', (prec), 'cantidad=', cant
                    productos.append(prod)
                    inventario.append(producto(prod, prec, cant))
        SoN = raw_input('\nagregar nuevo producto[s/n]: ')

    print '- FIN DEL INVENTARIO -\n'


# recibe una lista python con productos y retorna el indice de la lista 
# en que se encuentra el producto con 'nombre' o -1 si no existe
def indiceNombre(lista, nombre):
    if nombre in lista:
        return lista.index(nombre)
    return -1


# recibe una lista de productos e imprime en pantalla un producto por linea
# ej: "agua precio= $ 1000 cantidad= 10"
def imprimirProductos(lista):
    print''
    for i in lista:
        print i.nombre, '$', i.precio, 'cantidad:', i.cantidad


# suma el valor total de los productos de una lista, 
# considerando el stock de cada producto para calcular el valor
# Retorna el valor total de lista
def sumaProductos(lista):
    suma = 0
    for i in lista:
        suma = suma + i.cantidad * i.precio
    return suma


# muestra un dialogo que permite al usuario agregar productos a su carrito, 
# siempre y cuando el producto exista y tenga stock suficiente
# muestra un resumen de la compra realizada al finalizar
def comprar():
    compra = []
    print '\n- INICIANDO CARRITO DE COMPRAS -\n'
    SoN = 's'
    while SoN == 's':
        prodc = raw_input('- ingrese nombre del producto: ')
        if prodc in productos:
            ind = indiceNombre(productos, prodc)
            cantc = int(raw_input('- ingrese cantidad: '))
            if inventario[ind].cantidad < cantc:
                print inventario[ind].cantidad
                print '--- no hay suficiente', prodc, 'en stock!'
            else:
                inventario[ind].cantidad = inventario[ind].cantidad - cantc
                compra.append(producto(prodc, inventario[ind].precio, cantc))
                print '--- se agrego:', cantc, 'x', prodc
        else:
            print '--- el producto elegido no existe!'
        SoN = raw_input('\nagregar otro producto al carrito?[s/n]: ')

    print '\n-- RESUMEN DE LA COMPRA --'
    for i in compra:
        print i.nombre, '$', i.precio, 'cantidad=', i.cantidad
    print '--- total compra:', sumaProductos(compra), '\n'


#############################
# programa principal 
### no debe ser modificado!!

print "-- BIENVENIDO A LA TIENDITA --\n"
inventario=[] # variable global que almacena el inventario actualizado

crearInventario()
print "-- RESUMEN DE PRODUCTOS EN EL INVENTARIO --"
imprimirProductos(inventario)

comprar()
print "--- INVENTARIO ACTUALIZADO ---"
imprimirProductos(inventario)
