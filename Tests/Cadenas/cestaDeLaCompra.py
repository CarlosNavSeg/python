print("Introduzca los productos de la compra, separados por ',' ")
productos = str(input())
while(productos.__contains__(",")):
    productoDescompuesto = productos.replace(productos, productos[0:productos.index(",")])
    productos = productos.replace(productos, productos[productos.index(",")+1:len(productos)])
    print(productoDescompuesto)
print(productos)