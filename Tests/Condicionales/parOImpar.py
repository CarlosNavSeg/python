print("Introduzca un número entero")
numeroEntero = str(input())
numeroEntero = numeroEntero.replace(numeroEntero, numeroEntero[len(numeroEntero) -1: len(numeroEntero)])

numerospares = ["2", "4" , "6" , "8" , "0"]


if(numeroEntero in numerospares):
    print("Numero par")
else:
    print("Numero impar")