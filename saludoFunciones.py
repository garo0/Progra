# esDia: int -> bool
# Recibe una hora del dia y dice si corresponde a la mannana o no (entre 1<=x<12)
# Ej: esDia(12) == False
def esDia(hora):
    return hora < 12

# tests
assert esDia(12) == False

# esTarde: int -> bool
# Recibe una hora del dia y dice si corresponde a la tarde o no (entre 12<=x<21)
# Ej: esTarde(12) == True, esTarde(21) == False
def esTarde(hora):
    return hora >= 12 and hora < 21

# tests
assert esTarde(12) == True
assert esTarde(21) == False