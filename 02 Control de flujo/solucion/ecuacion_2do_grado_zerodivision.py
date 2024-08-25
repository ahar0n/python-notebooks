a = float(input('a? '))
if a != 0:
    b = float(input('b? '))
    c = float(input('c? '))

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
else:
    print('Para una cuadrática, a <> 0.')




































# test 1: delta > 0, a=1, b=5, c=1 => 2 Soluciones reales
# test 2: delta < 0, a=1, b=2, c=3 => Sol en complejos
# test 3: delta == 0, a=1, b=2, c=1 => Sol unica
# test 4: a=0, b=2, c=3 => No tiene solucion (o indeterminacion)