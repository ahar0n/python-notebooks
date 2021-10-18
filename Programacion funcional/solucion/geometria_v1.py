# areayperimetro.py determinacion de area y perimetro de un poligono
# Obs: en el ingreso de datos, debe cerrar el poligono.

def distancia(lado):
    '''distancia entre dos vectores'''
    dx = lado[1][0] - lado[0][0] # lado = [(3,4), (5,11)] => dx = 5 - 3
    dy = lado[1][1] - lado[0][1] # dy = 11 - 4
    return (dx ** 2 + dy ** 2) ** 0.5


def obtener_lados(vertices):
    '''lista de lados (distancia) de un poligono'''
    lista_lados = []
    for i in range(len(vertices)-1):
        lista_lados.append(distancia(vertices[i:i+2]))
    return lista_lados


def area(vertices):
    sumaXY = 0
    sumaYX = 0
    for i in range(len(vertices)-1):
        sumaXY += vertices[i][0] * vertices[i+1][1] # i=0 => x0 * y1
        sumaYX += vertices[i][1] * vertices[i+1][0] # i=0 => y0 * x1
    return (1/2) * abs(sumaXY - sumaYX)
        

def perimetro(vertices):
    lados = obtener_lados(vertices)
    suma = 0
    for lado in lados:
        suma += lado
    return suma


vertices = [ 
    (3,4), (5,11), (12,8), (9,5), (5,6), (3,4)
]
# i=0 => vertices[i:i+2] => [(3,4), (5,11)]
# i=1 => vertices[1:3] => [(5,11),(12,8)]
# dP1-P2, dP2-P3, dP3-P4, dP4-P5, dP5-P1

# vertices[0:1] == vertices[0]
# i=0; vertices[i:i+2] == vertices[0] + vertices[1]

print(perimetro(vertices))