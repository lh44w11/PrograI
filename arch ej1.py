#ej1

try:
    archivo = open("EJ 1.txt", "rt")
    mi_arch = open("arch.txt", "wt")
    
    linea = archivo.readline()
    
    while linea:
        guardar = True
        for i in range(len(linea)):
            if linea[i] == r'"' and linea[i+1] == r'"' and linea[i+2]== r'"' and guardar:
                guardar = not guardar
            elif linea[i] == r'#' and r'"' not in linea[i+1:]:
                guardar = False
            if guardar:
                mi_arch.write(linea[i])
            elif i == len(linea)-1 and not guardar:
                mi_arch.write("\n")
        linea = archivo.readline()
    
                
except FileNotFoundError:
    print("no se encontro el archivo")
except OSError:
    print("no se pudo grabar en el archivo")
    
finally:
    try:
        archivo.close()
        mi_arch.close()
    except NameError:
        pass