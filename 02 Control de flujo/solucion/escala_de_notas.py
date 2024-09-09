cantidad = int(input("¿Cuántas notas desea evaluar? "))
while cantidad > 0:
    nota = float(input("Ingrese nota: "))
    if nota >= 6:
        print("Excelente")
    elif nota >= 4:
        print("Buena")
    else:
        print("Mala")
    cantidad = cantidad - 1

