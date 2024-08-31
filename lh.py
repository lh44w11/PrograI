### PROGRAMA PRINCIPAL ###
try:
    leerArchivo = open("lh.txt", "rt", encoding="UTF8")
    escribirArchivo = open("lhh.txt", "wt")
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    
    linea = leerArchivo.readline()
    
    while linea:
        linea = linea.split(" ")
        for palabra in linea:
            sumvocales = 0
            for letra in palabra.lower():  
                if letra in vocales:       
                    sumvocales += 1
            if sumvocales>len(palabra)/2:
                palabra = "(" + palabra + ")"
                
            escribirArchivo.write(palabra + " ")
            
            if palabra.endswith("."):
                escribirArchivo.write("\n")
                    
        linea = leerArchivo.readline()

except FileNotFoundError:
    print("Error. No se encontro el archivo.")
except OSError:
    print("Error. No se pudo grabar en el archivo.")
except UnicodeError:
    print("Error. No se pudo leer el archivo.")
    
finally:
    try:
        leerArchivo.close()
        escribirArchivo.close()
    except NameError:
        pass

                    
                
        