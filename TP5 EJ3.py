### FUNCIONES ###
def devolverMes():
    try:
        lista = []
        n = int(input("Ingrese un numero de mes: "))
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
             "Diciembre"]
        assert 1<=n<=12
        n = n-1
        lista.append(meses[n])
        return lista
    except ValueError:
        print("Error. No se ingreso un numero natural.")
        return lista
    except AssertionError:
        print("Error. No se ingreso un numero entre uno y doce.")
        return lista
        
### PROGRAMA PRINCIPAL ###
print(devolverMes())

