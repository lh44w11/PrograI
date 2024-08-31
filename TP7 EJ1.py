### FUNCIONES ###
def cantidadDigitos(n, suma):
    if n==0:
        return suma
    else:
        n = n//10
        suma = suma + 1
        suma = cantidadDigitos(n, suma)
        
        return suma

### PROGRAMA PRINCIPAL ###
try:
    n = int(input("Ingrese un numero: "))
    suma = 0
    print(cantidadDigitos(n, suma))
except RecursionError:
    print("Error. Error de recursividad.")
except ValueError:
    print("Error. No se ingreso un valor correcto.")