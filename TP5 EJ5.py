### MODULOS ###
import math

### FUNCIONES ###
def calcularRaizCuadrada(n):
    while True:
        try:
            assert n>0
            resultado = math.sqrt(n)
            break
        except AssertionError:
            print("Error. No se ingreso un numero positivo.")
        
### PROGRAMA PRINCIPAL ###
while True:
    try:
        n = int(input("Ingrese un numero para calcular su raiz cuadrada: "))
        calcularRaizCuadrada(n)
        break
    except ValueError:
        print("Error. No se ingreso un valor valido.")

