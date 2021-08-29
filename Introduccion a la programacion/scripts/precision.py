longitud = float(input('Longitud (m): '))
error = float(input('Error (cm): '))

precision = longitud / (error/100)

print('Precision planimétrica es {}'.format(round(precision)))