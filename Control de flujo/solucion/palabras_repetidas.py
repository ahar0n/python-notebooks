texto = input('Ingrese texto: ')

# obtener texto sin puntuacion
texto_sin_puntuacion = ''
for char in texto:
    if char not in '¿?.¡!,-_':
        texto_sin_puntuacion += char


# separar palabras
palabras_texto = []
palabra = ''
for char in texto_sin_puntuacion:
    if char == ' ':
        palabras_texto.append(palabra)
        palabra = ''
    else:
        palabra += char
palabras_texto.append(palabra)  # se agrega la ultima palabra


# contar palabras
palabras_resumen = []   # ['puede', 'que', 'en'...]
cuenta_resumen = []     # [2, 2, 1,...]
for palabra_texto in palabras_texto:
    if palabra_texto not in palabras_resumen:
        palabras_resumen.append(palabra_texto)  # ['puede', 'que',...]
        cuenta_resumen.append(1)                # [2, 1,...,]
    else:
        index = palabras_resumen.index(palabra_texto)
        cuenta_resumen[index] = cuenta_resumen[index] + 1 # [1+1,1,...]


# preparar las salidas (aislar las repetidas)
repetidas = ''
cuenta = 0
for i in range(len(cuenta_resumen)):
    if cuenta_resumen[i] > 1:
        repetidas += palabras_resumen[i] + ', '
        cuenta += 1

print('Existen {} palabras repetidas: {}'.format(cuenta, repetidas[:-2]))