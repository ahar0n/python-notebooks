# solución con diseño basado en funciones

def valida_longitud(ppu):
    cuenta = 0
    for caracter in ppu:
        cuenta += 1
    if cuenta == 6:
        return True
    else:
        return False

def valida_bbbb(bbbb):
    respuesta = True
    for b in bbbb:
        if not(b in 'BCDFGHJKLPRSTVWXYZ'):
            respuesta = False
            break
    return respuesta

def valida_nn(nn):
    if nn < 10 or nn > 99:
        return False
    else:
        return True

def numero_dv(bbbb, nn):
    alfabeto_ppu = 'BCDFGHJKLPRSTVWXYZ'
    numerico_ppu = '123456789023456789'

    i = 1
    nd = 0
    while i <= len(bbbb):
        indice = alfabeto_ppu.index(bbbb[-i])
        ndi = int(numerico_ppu[indice])
        nd += ndi * 10 ** (i-1)
        i += 1
    ndv = nd * 100 + nn
    return ndv

def suma_ponderada(ndv):
    sp = 0
    i = 0
    while ndv > 0:
        di = ndv % 10
        ndv = ndv // 10
        sp += di * (i+2)
        i += 1
    return sp

def digito_verificador():
    ppu = input('Ingrese placa patente: ')

    # validación de la longitud de la PPU
    if valida_longitud(ppu):

        # validación del patron de letras
        bbbb = ppu[0:4]
        bbbb_valido = valida_bbbb(bbbb)

        # validación de la parte numérica
        try:
            nn = int(ppu[4:])
            nn_valido = valida_nn(nn)

        except ValueError:
            ppu_valida = False

        if bbbb_valido and nn_valido:
            ppu_valida = True
            # si la PPU es válida, caclula el DV
            ndv = numero_dv(bbbb, nn)
            sp = suma_ponderada(ndv)
            resto = sp % 11
            if resto == 10:
                dv = 'K'
            elif resto == 0:
                dv = 0
            else:
                dv = 11 - resto
        else:
            ppu_valida = False
    else:
        ppu_valida = False

    if ppu_valida:
        print(dv)
    else:
        print('PPU inválida')

    return

digito_verificador()