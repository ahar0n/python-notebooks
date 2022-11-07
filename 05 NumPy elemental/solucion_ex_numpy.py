import numpy as np

def valor_mas_cercano(escalar, vector):
    '''
    Encuentra en el vector el valor más cercano al escalar
    '''
    idx = (np.abs(vector - escalar)).argmin()
    return vector[idx]

def valores_comunes(a, b):
    '''
    Encuentra valores comunes en los arreglos a y b
    '''
    values = np.intersect1d(a, b)
    values_sorted = np.sort(values)
    return values_sorted[::-1]
    