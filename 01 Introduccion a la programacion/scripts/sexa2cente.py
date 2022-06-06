# Entradas
grados = int(input('Ingreses los grados: '))
minutos = int(input('Ingreses los minutos: '))
segundos = int(input('Ingreses los segundos: '))

# conversión a grados decimales
grados_decimales = grados + (minutos / 360) + (segundos / 3600)

# conversión sexa a cente
grados_centesimales = grados_decimales / 180 * 200

# Salidas
print("En grados centesimales es {:.4f}".format(grados_centesimales))