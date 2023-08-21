anio = int(input('Ingrese anio: '))

if anio % 400 == 0:
    respuesta = 'Es bisiesto'
else:
    if anio % 100 == 0:
        respuesta = 'Es normal'
    else:
        if anio % 4 == 0:
            respuesta = 'Es bisiesto'
        else:
            respuesta = 'Es normal'

print(respuesta)