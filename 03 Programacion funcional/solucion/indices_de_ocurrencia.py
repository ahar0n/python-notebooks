def indices(letra, palabra, idx=0):
    """Obtiene una lista con los indices de ocurrencia(s) de una letra en una palabra.

    Args:
        letra (str): Letra a buscar
        palabra (str): Palabra objetivo
        idx (int, optional): Indice de ocurrencia de la letra en la palabra. Por defecto 0.

    Returns:
        list: Lista de indices.
    """

    # caso base
    if len(palabra) == 0:
        return []

    else:
        primera_letra = palabra[0]
        segmento = palabra[1:]
        if letra == primera_letra:            
            return [idx] + indices(letra, segmento, idx+1)
        else:
            return indices(letra, segmento, idx+1)