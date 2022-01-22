def digitos(cifra):
    """Obtiene la cantidad de dígitos de una cifra.

    Args:
        cifra (int): Cifra de n dígitos.

    Returns:
        int: Cantidad de digitos.
    """
    
    # caso base
    if cifra < 10:
        return 1

    else:
        return 1 + digitos(cifra//10)