
def mostrar_alertas_stock(productos: list) -> None:
    print("\n==========ALERTAS DE INVENTARIO==========")

    proveedores = []

    for producto in productos:
        if producto["stock"] <= producto["stock_minimo"]:
            if producto["proveedor"] not in proveedores:
                proveedores.append(producto["proveedor"])

    if len(proveedores) == 0:
        print("no hay productos con alertas de stock.")
        return

    for proveedor in proveedores:
        print("\nProveedor:", proveedor)

        for producto in productos:
            if producto["proveedor"] == proveedor:
                if producto["stock"] <= producto["stock_minimo"]:
                    print("-----------------------------")
                    print("Codigo:", producto["codigo"])
                    print("Nombre:", producto["nombre"])
                    print("Stock actual:", producto["stock"])
                    print("Stock minimo:", producto["stock_minimo"])

                    if producto["stock"] == 0:
                        print("AGOTADO")
                    else:
                        print("STOCK BAJO")
