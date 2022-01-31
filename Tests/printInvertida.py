from traceback import print_stack


print("Introduzca una frase")
frase = str(input())
longitud = int(len(frase))
invertida = ""
while(longitud > 0):
   invertida += frase[longitud-1]
   longitud = longitud - 1

print(invertida)