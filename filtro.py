def filtrar_productos(productos, umbral, mayor_que):
    productos_filtrados = {}

#mayor-menor que umbral
    for producto, valor in productos.items():
        if mayor_que:
            if valor > umbral:
                productos_filtrados[producto] = valor
        else:
            if valor < umbral:
                productos_filtrados[producto] = valor

    return productos_filtrados 

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        umbral = int(sys.argv[1])
        if len(sys.argv) > 2:
            comparar = sys.argv[2]
            if comparar == 'otro':
                print("Lo sentimos, no es una operación válida")
                sys.exit()
            mayor_que = comparar == 'mayor'
        else:
            mayor_que = True
    else:
        umbral = 0
        mayor_que = True

    productos = {
        "Notebook" : 700000,
        "Teclado" : 25000,
        "Mouse" : 12000,
        "Monitor" : 250000,
        "Escritorio" : 135000,
        "Tarjeta de video" : 1500000
    }

#Debe arrojar los nombres de los productos(clave)  
    productos_filtrados = filtrar_productos(productos, umbral, mayor_que)
    if mayor_que:
        print("Los productos mayores al umbral son:")
    else:
        print("Los productos menores al umbral son:")
    for clave in productos_filtrados.keys():
        print(clave)

