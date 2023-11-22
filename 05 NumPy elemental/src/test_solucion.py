import numpy as np
from solucion_ex_numpy import valores_comunes

A = np.random.randint(0,10,10)
B = np.random.randint(0,10,10)

print(np.sort(A))
print(B)
print(valores_comunes(A, B))