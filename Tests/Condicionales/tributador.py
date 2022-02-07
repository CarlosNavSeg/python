print("Introduzca su edad: ")
edad = int(input())
print("Introduzca sus ingresos: ")
ingresos = int(input())
if(edad > 16 and ingresos >= 1000):
    print("Tributa")
else:
    print("No tributa")