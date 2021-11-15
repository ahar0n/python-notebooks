# primosentredosnumero.py
a = int(input('Número menor: '))
b = int(input('Número mayor: '))

dividendo = a + 1
while dividendo < b:
    divisor = dividendo - 1
    divisibles = 0
    while divisor > 1:
        if (dividendo % divisor) == 0:
            divisibles += 1
        divisor -= 1
    if not (divisibles > 0):
        print(dividendo)
    dividendo += 1