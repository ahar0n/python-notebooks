def cantidad_caracteres(cadena):
    """Obtiene la cantidad de caracteres de una cadena.

    Args:
        cadena (str): Cadena de caracteres.

    Returns:
        int: Cantidad de caracteres.
    """

    # caso base
    if len(cadena) == 0:
        return 0
        
    else:
        return 1 + cantidad_caracteres(cadena[1:])