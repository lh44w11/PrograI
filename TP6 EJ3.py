### FUNCIONES ###
def grabarRangoAlturas(deporte, altura, altura2):
    escribirArchivo.write(deporte)
    escribirArchivo.write("\n")
    escribirArchivo.write(f"Altura del primer atleta: {altura}")
    escribirArchivo.write("\n")
    escribirArchivo.write(f"Altura del segundo atleta: {altura2}")
    escribirArchivo.write("\n")
    
def grabarPromedio(deporte, altura, altura2):
    try:
        promedio = (altura+altura2) / 2
        escribirArchivo2.write(deporte)
        escribirArchivo2.write("\n")
        escribirArchivo2.write(f"Promedio de ambas alturas: {promedio}")
        escribirArchivo2.write("\n")
        
    except ZeroDivisionError:
        print("Error. No se pudo calcular el promedio.")
    
### PROGRAMA PRINCIPAL ###
try:
    escribirArchivo = open("TP6 EJ3 alturas.txt", "wt")
    escribirArchivo2 = open("TP6 EJ3 promedio.txt", "wt")
    
    vueltas = int(input("Cuantos deportes va a ingresar: "))
    for i in range(vueltas):
        deporte = input("Ingrese el deporte: ")
        altura = float(input("Ingrese la altura del primer atleta: "))
        altura2 = float(input("Ingrese la altura del segundo atleta: "))
        grabarRangoAlturas(deporte, altura, altura2)
        grabarPromedio(deporte, altura, altura2)
        
        
except ValueError:
    print("Error. No se ingreso un valor correcto.")
except FileNotFoundError:
    print("Error. No se encontro el archivo.")
except OSError:
    print("Error. No se pudo grabar en el archivo.")
    
finally:
    try:
        escribirArchivo.close()
        escribirArchivo2.close()
    except NameError:
        pass
    
    
    
    
    
    
    