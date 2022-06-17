anio = int(input('Ingrese anio: '))

multiplo_4 = anio % 4 == 0
multiplo_100 = anio % 100 == 0
multiplo_400 = anio % 400 == 0

bisiesto = (multiplo_4 and not multiplo_100) or multiplo_400

if bisiesto:
    print('Es bisiesto')
else:
    print('Es normal')