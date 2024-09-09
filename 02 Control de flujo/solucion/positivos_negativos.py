
cantidad = int(input("Cuántos números tiene la lista? "))

positivos = ''
negativos = ''

i = 1

while i <= cantidad:
    n = input(f"Ingrese n{i-1}: ")

    if int(n) > 0:
        if (positivos != '') and (i < cantidad):
            positivos += ',' + n
        else:
            positivos += n

    if int(n) < 0:
        if (negativos != '') and (i < cantidad):
            negativos += ',' + n
        else:
            negativos += n

    i += 1

print("Negativos:", negativos)
print("Positivos:", positivos)
