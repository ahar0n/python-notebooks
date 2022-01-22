l = float(input('distancia observada (m): '))
t = float(input('temperatura (ºC): '))
p = float(input('presion atmosferica (mmHg): '))

p_kpa = p * 1.3332

ka = ( 279.66 -  ((79.531*p_kpa)/(273.15+t)) ) * (10**(-6))
d = l * (1 + ka)

print('La distancia real es {:.3f} metros'.format(d))