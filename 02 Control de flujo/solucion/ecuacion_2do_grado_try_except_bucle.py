try:
    a = float(input('a? '))
    if a != 0:
        b = float(input('b? '))
        c = float(input('c? '))
        coeficientes_validos = True
    else:
        print('Para una ecuación de 2do grado, a <> 0.')
        coeficientes_validos = False
except ValueError:
    print('Debe ingresar valores numéricos.')
    coeficientes_validos = False

if coeficientes_validos:
    delta = b**2 - (4*a*c)

    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print('x1 = {}, x2 = {}'.format(x1, x2))
    elif delta == 0:
        x1 = -b / (2*a)
        x2 = x1
        print('x1 = {}; x2 = {}'.format(x1, x2))
    else:
        print('La solución no se encuentra en los reales!')





































# test 1: delta > 0, a=1, b=5, c=1 => 2 Soluciones reales
# test 2: delta < 0, a=1, b=2, c=3 => Sol en complejos
# test 3: delta == 0, a=1, b=2, c=1 => Sol unica
# test 4: a=0, b=2, c=3 => No tiene solucion (o indeterminacion)