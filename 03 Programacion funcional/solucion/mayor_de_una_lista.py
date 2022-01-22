def maximo(lista):
    """Obtiene el valor mayor de una lista.

    Args:
        lista (list): Lista de valores.

    Returns:
        int: Valor mayor.
    """
    
    # caso base
    if len(lista) == 1:
        return lista[0]

    else: 
        if lista[0] > maximo(lista[1:]):
            return lista[0]
        else:
            return maximo(lista[1:])