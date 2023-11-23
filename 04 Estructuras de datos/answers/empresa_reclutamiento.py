def leer_puntajes(nombre_archivo):
    archivo = open(nombre_archivo)
    puntajes = []
    while True:
        linea = archivo.readline()
        if linea == '':
            break
        puntajes += [float(linea)]
    archivo.close()

    return puntajes


def mejores_puntajes(nombre_archivo, cantidad):
    """
    Máximos puntajes
    Args:
        nombre_archivo (str): Nombre del archivo con valores numéricos
        cantidad (int): Cantidad de valores máxmios a encontrar. cantidad < len(valores_archivo)

    Returns:
        list(): Puntajes máximos, oredenados.
    """
    puntajes = leer_puntajes(nombre_archivo)

    mejores = []
    while len(mejores) < cantidad:
        el_maximo = maximo(puntajes)
        puntajes.remove(el_maximo)
        mejores.append(el_maximo)

    return mejores


def maximo(lista):
    el_maximo = lista[0]
    for i in lista[1:]:
        if i > el_maximo:
            el_maximo = i

    return el_maximo


def seleccion_de_puntajes(nombre_archivo, seleccionados=10, espera=3):
    mejores_30 = mejores_puntajes(nombre_archivo, seleccionados + espera)

    puntajes_seleccionados = mejores_30[:seleccionados]
    exportar_puntajes("../data/mejores_puntajes.txt", puntajes_seleccionados)

    puntajes_lista_espera = mejores_30[seleccionados:]
    exportar_puntajes("../data/lista_de_espera.txt", puntajes_lista_espera)

    return


def exportar_puntajes(nombre_archivo, contenido):
    archivo = open(nombre_archivo, "w")
    for i in contenido:
        archivo.write(f"{i}\n")
    archivo.close()


def promedio(nombre_archivo):
    puntajes = leer_puntajes(nombre_archivo)
    suma = 0
    for puntaje in puntajes:
        suma += puntaje

    promedio = suma / len(puntajes)

    return promedio


archivo_puntajes = "../data/lista_de_espera.txt"
print(promedio(archivo_puntajes))
