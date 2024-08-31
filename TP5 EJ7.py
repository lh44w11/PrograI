### LIBRERIAS ###
import random

### PROGRAMA PRINCIPAL ###
print("Bienvenido! Debe adivinar el numero entre 1 y 500.")
n = random.randint(1,500)
intentos = 1

while True:
    try:
        num = int(input("Ingrese un numero: "))
        assert 1<=num<=500
        if num==n:
            print("Felicidades, adivinaste el numero!")
            print("El numero era:", num)
            print("Lo encontraste en", intentos, "intentos!")
            break
        if num<n:
            print("El numero ingresado es menor.")
            intentos = intentos + 1
        if num>n:
            print("El numero ingresado es mayor.")
            intentos = intentos + 1
    except ValueError:
        print("Error. No se ingreso un numero natural.")
        intentos = intentos + 1
    except AssertionError:
        print("Error. No se ingreso un numero entre 1 y 500")