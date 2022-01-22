# localidades.py : biblioteca localidades

def get_localidades(file_name):
	localidades = []
	fichero = open(file_name, 'r')
	for linea in fichero:
		localidad = linea.rstrip().split(',')
		localidades.append( (localidad[0], localidad[1:]) )
	fichero.close()
	return localidades

def son_vecinas(diagrama, x, y):
	for localidad, vecinas in diagrama:
		if localidad == x and y in vecinas:
			return True
	return False

def existe_ruta(diagrama, ruta):
	for i in range(len(ruta)-1):
		if not son_vecinas(diagrama, ruta[i], ruta[i+1]):
			return False
	return True