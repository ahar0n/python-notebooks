def es_palindromo(palabra):
    """Verifica si una palabra es palindromo.

    Args:
        palabra (str): Palabra objetivo.

    Returns:
        bool: Verificador.
    """
    
    # caso base
    if len(palabra) == 1:
        return True

    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False