#ej1
#try:
#    n = int(input("ingrese un numero natural: "))
#    assert n>=1
#except ValueError:
#    print("no es un numero natural ")
#except AssertionError:
#    print("el numero debe ser mayor a 1")

#ej2
#def suma(cad1, cad2):
#    sumaa = -1
#    try:
#        numun = float(cad1)
#        numdo = float(cad2)
#        sumaa = numun+numdo
#    except ValueError:
#        print("debe ingresar numeros reales")
#    finally:
#        try:
#             return sumaa
#        except:
#            print("error")
#cad1 = input("ingrese numeros: ")
#cad2 = input("ingrese numeros: ")
#sumar = suma(cad1, cad2)
#print(f"la suma de {cad1} y {cad2} es: {sumar}")

#ej3

#def mes (numero):
#    letra = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
#    mees = letra[numero]
#    return mees
#try:    
#    numerom = int(input("ingrese numero del mes: "))
#    while numerom<1 or numerom>12:
#        numerom = int(input("ingrese numero del mes: "))
#    assert numerom>1 or numerom<12
#except ValueError:
#    print("debe ingresar un mes válido")
#except AssertionError:
#    print("numero de mes incorrecto")
#else:
#    ver = mes(numerom)
#    print(ver)


#ej4
#try:
#    i = 1
##    while i<100000:
#        print(i)
#        i+=1
#except KeyboardInterrupt:
#    print("\n------------")
#    print("apretaste ctrl+c")

#ej5
#import math
#def raiz(num):
#    raaiz = math.sqrt(num)
#    return raaiz
#try:
#    num = int(input("ingrese num: "))
#    assert num>0
#except AssertionError:
#    print("debiste ingresar un numero pos")
#else:
#    cuadrada = raiz(num)
#    print(f"la raiz cuadrada de {num} es {cuadrada}")

#ej6
#def busqueda(lista):
#    cont =0
#    while cont<3:
#        try:
#            valor = int(input("que valor desea buscar: "))
#            busc = lista.index(valor)
#        except ValueError:
#            print("no se encuentra en lista")
#            cont+=1
#        else:
#            return busc
#try:
#    n = int(input("ingrese nums: "))
#    lista = []
#    while n!=-1:
#        lista.append(n)
#        n = int(input("ingrese nums: "))
#except ValueError:
#    print("ingrese valor correcto")    
#else:
#    busco = busqueda(lista)
#    print(busco)

#ej7

# import random
# 
# def numerorand ():
#     n = random.randint(1,500)
#     return n
# 
# n = numerorand()
# cont = 0
# us = int(input("que numero salio?: "))
# while us!=n:
#     try:
#         if n>us:
#             print("el numero que ingresaste es menor")
#             cont+=1
#             us = int(input("que numero salio?: "))
#         else:
#             print("el numero que ingresaste es mayor")
#             cont+=1
#             us = int(input("que numero salio?: "))
#     except ValueError:
#         print("ingrese numeroooos")
#         cont+=1
#         us = int(input("que numero salio?: "))
#         
# else:
#     print(f"CORRECTO!, cant de intentos: {cont}")

    
#ej7 bis

#import random
#def numeroRand():
#    return random.randint(1,500)
#def ingresoNumeroConValidacion():
#    try:
#        us = int(input("Ingresa un número y adivina el número aleatorio?: "))
#    except ValueError:
#        print("El valor ingresado no es aceptado. Ingresa un valor correcto")
#        us  = "ERROR"
#     return us
# n = numeroRand()
# cont = 0
# us = ingresoNumeroConValidacion()
# while us == "ERROR":
#     cont+=1
#     us = ingresoNumeroConValidacion()
# while us != n:
#     if us > n:
#         print("Te fuiste muy arriba. Ingresa un numero más bajo")
#         cont+=1
#     else:
#         print("Te quedaste corto. Ingresa un numero más alto")
#         cont+=1
#     us = ingresoNumeroConValidacion()    
#     while us == "ERROR":
#         cont+=1
#         us = ingresoNumeroConValidacion()
# print("Felicitaciones! Adivinaste el numero aleatorio era: ",n)
# print("La cantidad de intentos fue: ",cont+1)