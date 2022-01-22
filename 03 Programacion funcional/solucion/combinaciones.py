# combinaciones.py numero de combinaciones formado por m elementos de un conjunto de n elementos

def factorial(x):
    '''Factorial del entero x.'''
    result = 1
    for i in range(x, 1, -1): # x=4 [4,3,2] => 4x1,4x3,12x2,
        result *= i
    return result


def valida_valores(n, m):
    '''Valida valores de entrada'''
    if n == 0:
        msg = 'Para calcular combinaciones, el conjunto debe contener elementos.'
        ans = False;
    elif n < 0 or m < 0:
        msg = 'Debe ingresar numeros positivos. Intente nuevamente!'
        ans = False;
    elif n < m:
        msg = 'Los valores no son coherentes, n debe ser mayor que m.'
        ans = False;
    elif m == 0:
        msg = 'No hay elementos para combinar. Intente nuevamente!'
        ans = False;
    else:
        msg = ''
        ans = True
    return (ans, msg)


def obtener_entradas(valores):
    '''Prepara las entradas'''
    n, m = valores.split(',')
    n = int(n)
    m = int(m)
    return (n, m)


def obtener_combinaciones(n, m):
    c = factorial(n) / ( factorial(n-m) * factorial(m))
    return c

# Programa principal
while True:
    
    valores = input('Ingrese valores de n y m separados por coma (Enter para salir): ')
    
    try:
        n, m = obtener_entradas(valores)
        son_validos, msg = valida_valores(n, m)
        
        if son_validos:
            c = obtener_combinaciones(n, m)
            print('El numero de combinaciones posibles es: {} '.format(c))
            break
        
        else:
            print(msg)

    except ValueError:
        print('Alguno de los valores ingresados no es válido. Intente nuevamente!')