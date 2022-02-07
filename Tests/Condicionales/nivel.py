print("Introduza su puntuación")
puntuacion = float(input())
if(puntuacion == 0.0):
    sueldo = 0
    print(sueldo)
elif(puntuacion == 0.4):
    sueldo = 2400*0.4
    print(sueldo)
elif(puntuacion >= 0.6):
    sueldo = 2400*puntuacion
    print(sueldo)
else:
    print("Valor incorrecto")
