a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a > b:       
    if a > c:
        mayor = a
        if b > c:
            medio = b
            menor = c           # a-b-c
        else:
            medio = c
            menor = b           # a-c-b
    else:
        mayor = c
        medio = a
        menor = b               # c-a-b
else:
    if b > c:
        mayor = b
        if a > c:
            medio = a
            menor = c           # b-a-c
        else:
            medio = c
            menor = a           # b-c-a
    else:
        mayor = c
        medio = b
        menor = a               # c-b-a

print('Números ordenados: {}-{}-{}'.format(menor, medio, mayor))