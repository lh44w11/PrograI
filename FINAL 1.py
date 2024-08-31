### LIBRERIAS ###
import random

### FUNCIONES ###
def armarTriangulo(lista):
    if len(lista) == 1:
        return [lista]
    else:
        filaSuperior = []
        for i in range(len(lista) - 1):
            suma = lista[i] + lista[i+1]
            filaSuperior.append(suma)
            filaInferior = armarTriangulo(filaSuperior)
            filaInferior.append(lista)
    
        return filaInferior
        
### PROGRAMA PRINCIPAL ###
largolista = int(input("Ingrese el largo de la lista: "))
lista = [random.randint(0,9) for i in range(largolista)]

triangulo = armarTriangulo(lista)
for i in triangulo:
    print(i)
    