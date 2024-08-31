### PROGRAMA PRINCIPAL ###
try:
    leerArchivo = open("TP6 EJ1 old.txt", "rt")
    escribirArchivo = open("TP6 EJ1 new.txt", "wt")
    
    linea = leerArchivo.readline()
    
    while linea:
        guardar = True
        for i in range(len(linea)):
            if linea[i] == r'"' and linea[i+1] == r'"' and linea[i+2] == r'"':
                guardar = False
            if linea[i] == r'#':
                guardar = False
            if guardar:
                escribirArchivo.write(linea[i])
            if i == len(linea)-1 and guardar = False:
                escribirArchivo.write("\n")
        
        linea = leerArchivo.readline()

except FileNotFoundError:
    print("Error. No se encontro el archivo.")
except OSError:
    print("Error. No se pudo grabar en el archivo.")

finally:
    try:
        leerArchivo.close()
        escribirArchivo.close()
    except NameError:
        pass
                
            
                
            
    
    
    