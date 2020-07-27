agenda={"Andres":22234646,"Maria":98723456,"David":43335555}

def agregar(agenda, nombre, fono):
    if nombre in agenda.keys():
        print 'Este nombre ya existe'
        return
    agenda[nombre] = fono


def borrar(agenda, nombre):
    if nombre not in agenda.keys():
        print 'Este nombre no se encuentra en la agenda'
        return
    del agenda[nombre]


def cambiar(agenda, nombre, fono):
    if nombre not in agenda.keys():
        print 'Este nombre no se encuentra en la agenda'
        return
    agenda[nombre] = fono
