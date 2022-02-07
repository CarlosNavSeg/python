numeroEntero = int(input())
contador = int(1)
print(contador)
while(numeroEntero > contador):  
    contador = contador+2
    print(contador)
    if(contador+1 > numeroEntero):
        break
