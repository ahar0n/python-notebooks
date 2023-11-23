import os

def corregir_resumen(nombre_archivo):

    # validar que el archivo existe
    if os.path.exists(nombre_archivo):

        texto_corregido_lista = corregir_mayusculas(nombre_archivo)
        texto_como_string = lista_a_texto(texto_corregido_lista)

        print(texto_como_string)

    else:
        print('Error, el archivo no existe!')


def lista_a_texto(lista):

    texto = ''
    for elemento in lista:
        texto += elemento

    return texto


def corregir_mayusculas(nombre_archivo):

    texto_como_lista = texto_a_lista(nombre_archivo)

    # la primera letra siempre será minuscula
    texto_como_lista[0] = texto_como_lista[0][0].upper() + texto_como_lista[0][1:]

    # se itera en longitud-2, para tener un alcance de tres elementos y evitar error de índice
    for i in range(len(texto_como_lista)-2):

        # para los casos de inicio de exclamación e interrogación, respectivamente
        if texto_como_lista[i] in '¿¡':        # elemento actual
            original = texto_como_lista[i+1]
            nueva = original[0].upper() + original[1:]

            texto_como_lista[i+1] = nueva

        # para los casos de fin de exclamación e interrogación, respectivamente
        if texto_como_lista[i] in '.!?':        # elemento actual
            original = texto_como_lista[i+2]
            nueva = original[0].upper() + original[1:]

            texto_como_lista[i+2] = nueva

    return texto_como_lista


def texto_a_lista(nombre_archivo):
    archivo_texto = open(nombre_archivo)
    lista = []
    palabra = ''

    while True:

        char = archivo_texto.read(1)

        if char != '':
            if char in ' .¡!¿?':
                if palabra != '':
                    lista.append(palabra)
                    palabra = ''
                lista.append(char)
            else:
                palabra += char

        else:
            break

    archivo_texto.close()
    return lista


def exportar_resumen_corregido(archivo_original, nuevo_archivo):

    texto_corregido_list = corregir_mayusculas(archivo_original)
    texto_como_string = lista_a_texto(texto_corregido_list)

    ruta = obtener_ubicacion(archivo_original)

    fid = open(f"{ruta}{nuevo_archivo}", "w")
    fid.write(texto_como_string)
    fid.close()

    return


def obtener_ubicacion(nombre_archivo):

    carpetas = []
    carpeta = ''
    for char in nombre_archivo:
        if char == '/':
            carpetas.append(carpeta)
            carpeta = ''
        else:
            carpeta += char

    ubicacion = ''
    for carpeta in carpetas:
        ubicacion += carpeta + "/"
    return ubicacion


nombre_archivo = "../data/resumen_minusculas.txt"
exportar_resumen_corregido(nombre_archivo, "resumen_corregido.txt")
