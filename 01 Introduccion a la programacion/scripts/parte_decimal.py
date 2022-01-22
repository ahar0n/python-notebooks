numero = input('Numero: ')
punto = numero.index('.')

decimal = numero[punto+1:]

print('La prate decimal es {}'.format(decimal))