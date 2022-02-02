print("Fecha de tu nacimiento en formato dd/mm/aa: ")
fecha = str(input())
while(fecha.__contains__("/")):
    fechaDescompuesta = fecha.replace(fecha, fecha[0:fecha.index("/")])
    fecha = fecha.replace(fecha, fecha[fecha.index("/")+1:len(fecha)])
    if(len(fechaDescompuesta) == 1):
        print("0" + fechaDescompuesta)
    else:
        print(fechaDescompuesta)
print(fecha)
    