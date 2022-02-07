n = int(input("Introduce un número entero positivo: "))
for i in range(n, 0, -1):
    print(i, end=", ")
    if(i == 1):
        print("0")