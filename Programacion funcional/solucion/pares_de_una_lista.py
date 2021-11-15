def pares(lista):
    """Obtiene los números pares de una lista de números.

    Args:
        lista (list): Lista de numeros.

    Returns:
        list: Lista de numeros pares.
    """
    
    # caso base
    if len(lista) == 0:
        return []
    
    else:
        entero = lista[0]
        restantes = lista[1:]
        if entero % 2 == 0:
            return [entero] + pares(restantes)
        else:
            return pares(restantes)