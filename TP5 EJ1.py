### FUNCIONES ###
def ingresarNumNatural():
    while True:
        try:
            n = int(input("Ingrese un numero natural: "))
            assert n>0
            return n
        except ValueError:
            print("Error. No se ingreso un numero natural.")
        except AssertionError:
            print("Error. El numero debe ser mayor a cero.")

### PROGRAMA PRINCIPAL ###
print(ingresarNumNatural())