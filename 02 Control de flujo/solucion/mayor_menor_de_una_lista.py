numeros = input('Ingrese lista de numeros: ')

# lista de numeros
lista_numeros = [] 
digito = ''
for char in numeros:
    if char == ',':
        lista_numeros.append(int(digito)) 
        digito = '' 
    else:
        digito = digito + char 

lista_numeros.append(int(digito)) # agregar ultimo digito


# mayor y menor
mayor = lista_numeros[0]
menor = lista_numeros[0]

for n in lista_numeros[1:]:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n


# almacenar en una tupla
mayor_menor = mayor, menor


# salidas
print('Mayor: {}, Menor: {}'.format(mayor, menor))