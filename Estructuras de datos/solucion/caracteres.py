def caracteres(texto):
    """Obtiene cuenta agrupada de caracteres de en un texto.

    Args:
        texto (str): Texto.

    Returns:
        dict: Cuenta agrupada de caracteres.
    """
    cuenta = {}
    for char in texto:
        if char == ' ': 
            continue
        else:
            if char.lower() not in cuenta:
                cuenta[char.lower()] = 1
            else:
                cuenta[char.lower()] += 1
    return cuenta