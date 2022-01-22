# primosgemelos.py muestra primos gemelos entre dos numero
# restricción: a < b
a = int(input('Número menor: '))
b = int(input('Número mayor: '))

dividendo = a + 1
primo_anterior = 0
while dividendo < b:
    divisor = dividendo - 1
    divisibles = 0
    while divisor > 1:
        if (dividendo % divisor) == 0:
            divisibles += 1
        divisor -= 1
    if not (divisibles > 0):
        primo = dividendo
        if (primo_anterior != 0) and (primo - primo_anterior == 2):
            print('({},{})'.format(primo_anterior, primo))
        primo_anterior = primo
    dividendo += 1