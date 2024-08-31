### LIBRERIAS ###
import random

### FUNCIONES ###
def crearMatriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    
    return matriz

def rellenarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            n = random.randint(0, 9)
            matriz[f][c] = n
            
def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()
        
def recorrerYsumar(matriz, f, c):
    suma = 0
    
            
### PROGRAMA PRINCIPAL ###
n = int(input("Ingrese un numero: "))
while n<3:
    n = int(input("Numero invalido. Ingrese un numero: "))
filas = n
columnas = n
matriz = crearMatriz(filas, columnas)
rellenarMatriz(matriz)
imprimirMatriz(matriz)

f = int(input("Ingrese un numero f: "))
c = int(input("Ingrese un numero c: "))
while f>=n or c>=n:
    f = int(input("Numero invalido. Ingrese un numero f: "))
    c = int(input("Numero invalido. Ingrese un numero c: "))
    
    

    
