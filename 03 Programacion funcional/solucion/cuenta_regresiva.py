
def regresiva_iterativa(n):
    """Muestra cuenta regresiva desde un número dado.

    Args:
        n (int): Numero inicial de la cuenta regresiva
    """

    for i in range(n, -1, -1):
        print(i)
    

def regresiva_recursiva(n):
    """Muestra cuenta regresiva desde un número dado.

    Args:
        n (int): Numero inicial de la cuenta regresiva

    Returns:
        int: Estado de la cuenta regresiva
    """

    # caso base
    if n == 0:
        return n
    
    else:
        print(n)
        return regresiva_recursiva(n-1)