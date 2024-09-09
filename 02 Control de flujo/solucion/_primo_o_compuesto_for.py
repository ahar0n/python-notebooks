natural = int(input('Ingresa un número: '))
divisores = 0
for i in range(1,natural,1):
    resto = natural % i
    if resto == 0:
        divisores = divisores + 1
if divisores > 1:
    print(f'El número {natural} es compuesto.')
else:
    print(f'El número {natural} es primo.')