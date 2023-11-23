# Ej. 1
def caracteres(texto):
    resultado = {}
    for char in texto:
        char = char.lower()
        if char in ' ':
            continue
        else:
            if char in resultado.keys():
                resultado[char] += 1
            else:
                resultado[char] = 1

    return resultado


# Ej. 2
def longitud(texto):
    cuenta = {}
    while len(texto) > 0:
        if ' ' in texto:
            # obtiene palabra si texto contiene espacios
            index_espacio = texto.index(' ')
            palabra = texto[:index_espacio]
        else:
            # obtiene palabra si texto no contiene espacios
            palabra = texto

        # eliminar puntuación de la palabra
        palabra_limpia = ''
        for letra in palabra:
            if letra in '.,¡!¿?':
                continue
            palabra_limpia += letra

        cuenta[palabra_limpia] = len(palabra_limpia)

        # re-asignar texto restante
        texto = texto[index_espacio + 1:]

    return cuenta


# Ej. 3
def lista_de_palabras(texto):
    palabras = []
    while len(texto) > 0:
        if ' ' in texto:
            # obtiene palabra si texto contiene espacios
            index_espacio = texto.index(' ')
            palabra = texto[:index_espacio]
            texto = texto[index_espacio + 1:]  # texto restante
        else:
            # obtiene palabra si texto no contiene espacios
            palabra = texto
            texto = ''  # texto restante

        # eliminar puntuación de la palabra
        palabra_limpia = ''
        for letra in palabra:
            if letra in '.,¡!¿?':
                continue
            palabra_limpia += letra

        palabras.append(palabra_limpia)

    return palabras


def cuenta_palabras(texto):
    cuenta_completa = cuenta_todas_las_palabras(texto)
    cuenta_repetidas = {}
    for palabra, cuenta in cuenta_completa.items():
        if cuenta > 1:
            cuenta_repetidas[palabra] = cuenta

    return cuenta_repetidas


def cuenta_todas_las_palabras(texto):
    palabras = lista_de_palabras(texto)
    cuenta = {}
    for palabra in palabras:
        if palabra not in cuenta.keys():
            cuenta[palabra] = 1
        else:
            cuenta[palabra] += 1
    return cuenta




# Pruebas
texto = 'Este texto no es solo un texto aleatorio, es un texto intensionado.'
print(cuenta_todas_las_palabras(texto))
