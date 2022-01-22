
def raiz(n, divisor=2):
    return n ** (1/divisor)

def distancia(a, b):
    return raiz((a[0] - b[0])**2 + (a[1] - b[1])**2)

def obtener_lados(vertices):
    lados = []
    for i in range(len(vertices)-1):
        lado = distancia(vertices[i], vertices[i+1])
        lados.append(lado)
    return lados

def area(vertices):
    p_cerrado = poligono_cerrado(vertices)
    sumaXY = 0
    sumaYX = 0
    for i in range(len(p_cerrado)-1):
        sumaXY += p_cerrado[i][0] * p_cerrado[i+1][1]
        sumaYX += p_cerrado[i+1][0] * p_cerrado[i][1]
    return 0.5 * abs(sumaXY - sumaYX)
        
def perimetro(vertices):
    lados = obtener_lados(poligono_cerrado(vertices))
    suma = 0
    for lado in lados:
        suma += lado
    return suma

def poligono_cerrado(vertices):
    return vertices + [vertices[0]]
