### FUNCIONES ###
def crearMatriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    
    return matriz
    
def rellenarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            n = int(input("Ingrese un valor: "))
            matriz[f][c] = n

def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()
        
### PROGRAMA PRINCIPAL ###
filas = int(input("Ingrese nº filas: "))
columnas = int(input("Ingrese nº columnas: "))
matriz = crearMatriz(filas, columnas)
rellenarMatriz(matriz)
imprimirMatriz(matriz)
