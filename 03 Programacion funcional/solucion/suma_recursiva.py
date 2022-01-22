def suma_enteros(lista):
    """Obtiene suma de números de una lista.

    Args:
        lista (list): Lista de números

    Returns:
        float: Suma
    """

    # condicion base
    if len(lista) == 0:
        return 0

    # caso recursivo
    # Descomponer el problema original en pequeñas instancias del mismo
    # el input es un dato estructurado que puede descomponerse recursivamente.
    else:
        el_primero = lista[0]
        segmento = lista[1:]
        return el_primero + suma_enteros(segmento)


def suma_enteros_v2(lista):
    """Obtiene suma de números de una lista.

    Args:
        lista (list): Lista de números

    Returns:
        float: Suma
    """

    # caso base
    if len(lista) == 1:
        return lista[0]

    # caso recursivo
    else:
        return lista[0] + suma_enteros_v2(lista[1:])