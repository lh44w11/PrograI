#ej1

# def recursion(n, dig):
#     while n!=0:
#         dig +=1
#         n//=10
#         recursion(n,dig)
#     return dig
# try:
#     n = int(input("ingrese un num entero: "))
#     dig = 0
#     assert n>0
# except ValueError:
#     print("debe ingresar un numero")
# except AssertionError:
#     print("debe ingresar num mayor a 0")
# else:
#     valor = recursion(n, dig)
#     print(f"cant digitos: {valor}")

#ej2

# def bin_dec(n,i=0,conversion = 0):
#    try:
#        while i<len(n):
#            if n[i] == "1":
#                conversion+=(2**i)
#            i+=1
#            bin_dec(n,i, conversion)
#    except ZeroDivisionError:
#        print("error rarooo")
#    else:
#        return conversion
# try:
#    n = input("ingrese un numero binario:")
#    n = list(n)
#    n.reverse()
#    
# except ValueError:
#    print("debes ingresar un numero binario")
# else:
#    decimal = bin_dec(n)
#    print(f"NUMERO DECIMAL: {decimal}")

#ej3

# def suma(N, mas = 0, indice = 1):
#     try:
#         while indice<=N:
#             mas = mas+(indice)
#             indice+=1
#             suma(N, mas, indice)
#     except RecursionError:
#         print("demasiados numeros")
#         
#     else:
#         return mas
# try:
#     N = int(input("ingrese un numero: "))
#     assert N>0
#  
# except ValueError:
#     print("debes ingresar un numero natural")
# except AssertionError:
#     print("debes ingresar un numero mayor a 0")
# else:
#     rec = suma(N)
#     print(f"suma de primeros numeros nat hasta {N}: {rec}")

#ej4

# def producto (a, b, suma = 0):
#     while b!=0:
#         suma+=a
#         b-=1
#         producto(a,b,suma)
#     return suma
# try:
#     a = int(input("ingrese num: "))
#     b = int(input("ingrese num: "))
#     
# except ValueError:
#     print("debe ingresar NUMEROSSSS")
# else:
#     mult = producto(a, b)
#     print(f"el producto entre {a} y {b} es: {mult}")

#ej5

# def division (a, b ):   
#     while a>=b:
#         a -=b
#         division(a,b)
#     return a
# try:
#     a = int(input("ingrese num: "))
#     b = int(input("ingrese num: "))
# except ValueError:
#     print("DEBE INGRESAR N U M E R O S")
# else:
#     div = division(a,b)
#     print(f"el resto entre la division de {a} y {b} es: {div}")

#ej6

# def A (m, n):
#     try:
#         if m == 0:
#             return n+1
#         if n == 0:
#             return A(m-1,1)
#         else:
#             return A(m-1, A(m,n-1))
#     except RecursionError:
#         print("error de recursion")
# for m in range(3):
#     for n in range(7):
#         print(f"A({m},{n}) = {A(m,n)}")

#ej7
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# def mcd(a,b):
#     if b == 0:
#         return 1
#     elif b>:
#         return mcd(b, a%b)
#     
# def calcularlo (lista):
#     if len(lista)==2:
#         mcd(lista[0], lista[1])
#     elif len(lista)>2:
#         mcd(lista[0], calcularlo(lista[1:]))
#     else:
#         return 1
# 
# try:
#     n = int(input("ingrese nums: "))
#     lista =[]
#     while n!=-1:
#         lista.append(n)
#         n = int(input("ingrese nums: "))
# except ValueError:
#     print("debe ingresar un numero")
# except AssertionError:
#     print("ingresaste un numero negativo")
# else:
#     mcdd = calcularlo(lista)
#     print(f"el mcd de los elementos de la lista {lista}, es: {mcdd}")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#ej8

# def ordenar (lista, i = 0):
#     try:
#         if i == len(lista)-1:    ####para que no haya indexerror!
#             return
#         
#         for j in range(i+1, len(lista)):
#             if lista[j]<lista[i]:
#                 lista[j], lista[i] = lista[i], lista[j]
#                 
#         ordenar(lista, i+1)
#     except RecursionError:
#         print("error de recursion")
#     except IndexError:
#         print("error con pos de listas")
#     else:
#         return lista
# 
# try:
#     n = int(input("ingrese nums: "))
#     lista = []
#     while n!=-1:
#         lista.append(n)
#         n = int(input("ingrese nums: "))
#         
# except ValueError:
#     print("debe ingresar numeros")
# else:
#     lista_orden = ordenar(lista)
#     print(f"lista ordenada: {lista_orden}")

#ej9
# import random
# 
# def crear_matriz(m,n):
#     mat = [[0]*n for i in range(m)]
#     return mat
# def datos (matriz, m, n):
#     for f in range(m):
#         for c in range(n):
#             x = random.randint(1,50)
#             matriz[f][c] = x
#     return matriz
# 
# def imprimir_mat (matriz, indice=0):
#     if indice>=len(matriz[0]):
#         return
#     
#     for elemento in matriz:
#         print(f"{elemento[indice]:6}", end= " ")
#     print()
#     indice+=1
#     imprimir_mat(matriz, indice)
#    
# try:
#     M = int(input("ingrese filas: "))
#     N = int(input("ingrese columnas: "))
#     assert M>0 and N>0
#     
# except ValueError:
#     print("debe ingresar un numero!!!")
# except AssertionError:
#     print("debe ingresar numeros positivos")
#     
# else:
#     matrix = crear_matriz(M,N)
#     data = datos(matrix, M, N)
#     imprimir_mat(data)

#10
# import random
# 
# def crear_mat(m,n):
#     matriz = [[0]*n for i in range(m)]
#     return matriz
# def datos_mat(mat, m, n):
#     for f in range(m):
#         for c in range(n):
#             x = random.randint(1,50)
#             mat[f][c] = x
#     return mat
# def impresion (mat, i = 0):
#     if i == len(mat[0]):
#         return
#     for elemento in mat:
#         print(f"{elemento[i]:6}", end= " ")
#     print()
#     i+=1
#     impresion(mat,i)
# def suma_matriz(mat, m, suma=0, i=0):
#     try:
#         while i<m:
#             lista = list(mat[i])
#             suma += sum(lista)
#             i+=1
#             suma_matriz(mat,m,suma, i)
#     except RecursionError:
#         print("error de recursion!")
#     else:
#         return suma
# try:
#     m = int(input("cant filas: "))
#     n = int(input("cant column: "))
# except ValueError:
#     print("debe ingresar numeros")
# except KeyboardInterrupt:
#     print("has detenido la impresion con ctrl+c")
#     
# else:
#     mi_mat = crear_mat(m,n)
#     dat = datos_mat(mi_mat, m,n)
#     impresion(dat)
#     mi_suma = suma_matriz(dat,m)
#     print(f"La suma de todos los elementos de la matriz es: {mi_suma}")

#ej11

# import random
# def crear(m,n):
#     mat = [[0]*n for i in range(m)]
#     return mat
# def datos(mat,m,n):
#     for f in range(m):
#         for c in range(n):
#             x = random.randint(1,50)
#             mat[f][c] = x
#     return mat
# def impresion(mat, indice = 0):
#     if indice == len(mat[0]):
#         return
#     for elemento in mat:
#         print(f"{elemento[indice]:6}", end= " ")
#     print()
#     indice+=1
#     impresion(mat,indice)
# def menor_y_pos(mat, m, n, i=0):
#     lista = list(x for fila in mat for x in fila)
#     minimo = min(lista)
#     for i in range(len(lista)):
#         if lista[i] == minimo:
#             f = i//m
#             c = i%n
#             pos = list[(f,c)]
#         else:
#             i+=1 
#     return minimo, pos
# try:
#     m = int(input("ingrese filas: "))
#     n = int(input("ingrese columnas: "))
#     assert m>0 and n>0
# except ValueError:
#     print("debe ingresar numeros!")
# except AssertionError:
#     print("debe ingresar num>0:")
# else:
#     mi_mat = crear(m,n)
#     dat = datos(mi_mat, m, n)
#     impresion(dat)
#     men, pos = menor_y_pos(dat, m, n)
#     print(f"el menor valor de la matriz es: {men}, y su posicion es: {pos}")

####fibonacci = sucesion infinita de numeros naturales, comienza con 0 y 1

# def fibonacci(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# 
# n = int(input("ingrese num: "))
# fib = fibonacci(n)
# print(fib)






    
    
    
    
    

    
    