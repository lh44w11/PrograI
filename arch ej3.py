#ej3

#funcion

def impresion(archivo):
    for grabacion in archivo:
        print(f"{grabacion}")
def GrabarRangoAlturas(deporte, alturas):
    rango.write(f"{alturas}\n")
    
def GrabarPromedio(suma, cont):
    try:
        promedio = suma/cont
        prom.write(f"{promedio}\n")
        
    except ZeroDivisionError:
        print("No se encontraron elementos para calcular promedio")
    
#pp
try:        
    dep = input("ingrese deporte: ")
    alt = float(input("ingrese alturas: "))
    rango = open("arch.txt", "wt")
    prom = open("archdos.txt", "wt")
    while dep!= "basta":
        rango.write(f"{dep}\n")
        prom.write(f"{dep}\n")
        suma = 0
        cont = 0
        while alt!=-1:
            GrabarRangoAlturas(dep,alt)
            suma= suma+alt
            cont+=1
            alt = float(input("ingrese alturas: "))
        GrabarPromedio(suma, cont)

        dep = input("ingrese deporte: ")
        alt = float(input("ingrese alturas: "))
    
except OSError:
        print("no se pudo grabar el archivo")
except ValueError:
        print("ingresaste un dato invalido")
finally:
    try:
        rango.close()
        prom.close()
    except NameError:
        pass
    try:
        archivo = open("arch.txt", "rt")
        leo = open("archdos.txt", "rt")
       
    except FileNotFoundError:
        print("no se encuentra el archivo")
    else:
        print("Rango de alturas: ")
        impresion(archivo)
        print("Promedios por alturas: ")
        impresion(leo)
        
       
        
    finally:
        try:
            archivo.close()
            leo.close()
        except NameError:
            pass
        

    