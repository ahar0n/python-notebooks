xa = float(input('Coordenada x de A? '))
ya = float(input('Coordenada y de A? '))
xb = float(input('Coordenada x de B? '))
yb = float(input('Coordenada y de B? '))
xc = float(input('Coordenada x de C? '))
yc = float(input('Coordenada y de C? '))

dab = ( (xb-xa)**2 + (yb-ya)**2 )**0.5
dbc = ( (xc-xb)**2 + (yc-yb)**2 )**0.5
dac = ( (xc-xa)**2 + (yc-ya)**2 )**0.5

s = (dab + dbc + dac) / 2
area = (s*(s-dab)*(s-dbc)*(s-dac)) ** 0.5

print(f'El area es {area}')
# Test a(0,0) b(0,3) c(4,0) => area es 6