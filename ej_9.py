import estructura

estructura.mutable("registro","nombre fono")
#agenda: list(registro)
agenda=[registro("a",2),registro("c",1),registro("d",4)]


def buscar(nombre, agenda):
    for i in range(len(agenda)):
        if agenda[i].nombre == nombre:
            return agenda[i].fono
    return 'El nombre consultado no esta en la agenda'
