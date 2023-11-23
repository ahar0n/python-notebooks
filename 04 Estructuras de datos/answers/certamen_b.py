
def restriccion(digitos, PPU, dia):
    x = PPU[-1]
    x = int(x)
    for i in digitos:
        dia_dig, numeros_dig = i
        if dia_dig == dia:
            if x in numeros_dig:
                return True
    return False


def con_restriccion(digitos, PPU):
    dias = []
    x = PPU[-1]
    x = int(x)
    for i in digitos:
        dia_digitos, numeros_digitos = i
        if x in numeros_digitos:
            dias.append(dia_digitos)
    return dias

digitos = [("lunes", [3, 4, 5, 6]),
           ("martes", [7, 8, 9, 0]),
           ("miercoles", [1, 2, 3, 4]),
           ("jueves", [5, 6, 7, 8]),
           ("viernes", [9, 0, 1, 2])
           ]

print(con_restriccion(digitos, "BBDT35"))