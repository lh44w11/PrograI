try:
    archivoViejo = open("hp.txt", "rt", encoding="UTF8")
    archivoNuevo = open("hpp.txt", "wt")
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

    linea = archivoViejo.readline()
    while linea:
        linea = linea.split(" ")
        for palabra in linea:
            contador = 0
            for i in range(len(vocales)):
                if vocales[i] in palabra or vocales[i] in palabra.lower():
                    contador = contador + 1
            
            if contador>len(palabra)/2:
                palabra = "(" + palabra + ")"
                
            archivoNuevo.write(palabra + " ")
            
        linea = archivoViejo.readline()
        
except FileNotFoundError:
    print("Sofi te amo pero no esta el archivo.")
except OSError:
    print("Sofi perdonanos no pudimos escribir el archivo.")
except UnicodeError:
    print("Sofi perdonanos no pudimos leer el archivo.")
    
finally:
    try:
        archivoViejo.close()
        archivoNuevo.close()
    except NameError:
        pass
        
    
    