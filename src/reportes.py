from datetime import date
from persistencia import cargar_ventas

def mostrar_alertas_stock(productos: list) -> None:
    print("\nALERTAS DE INVENTARIO")

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


def generar_reporte_diario(productos: list) -> None:
    print("\nREPORTE DIARIO")

    ventas = cargar_ventas()
    fecha_actual = date.today().isoformat()

    total_vendido = 0
    cantidad_ventas = 0
    productos_vendidos = {}
    categorias_movimiento = []

    # Revisar las ventas del dia
    for venta in ventas:
        datos = venta.split("|")

        if len(datos) != 3:
            print("se omitio una venta incorrecta.")
            continue

        if datos[0] == fecha_actual:
            try:
                total = float(datos[1])
                total_vendido += total
                cantidad_ventas += 1

                detalles = datos[2].split(";")

                for detalle in detalles:
                    codigo, cantidad = detalle.split(":")
                    cantidad = int(cantidad)

                    if codigo not in productos_vendidos:
                        productos_vendidos[codigo] = 0

                    productos_vendidos[codigo] += cantidad

            except ValueError:
                print("se omitio una venta incorrecta.")

    print("\nfecha:", fecha_actual)
    print("total vendido $", total_vendido)
    print("numero de ventas:", cantidad_ventas)

    if cantidad_ventas > 0:
        promedio = total_vendido / cantidad_ventas
        print("ticket promedio $", promedio)

        codigo_mas_vendido = max(
            productos_vendidos,
            key=productos_vendidos.get
        )

        for producto in productos:
            if producto["codigo"] == codigo_mas_vendido:
                print(
                    "producto mas vendido:",
                    producto["nombre"],
                    "- unidades:",
                    productos_vendidos[codigo_mas_vendido]
                )

        print("\nPRODUCTOS SIN VENTAS")

        for producto in productos:
            if producto["codigo"] not in productos_vendidos:
                print(producto["nombre"])

        print("\nCATEGORIAS CON MOVIMIENTO")

        for producto in productos:
            if producto["codigo"] in productos_vendidos:
                if producto["categoria"] not in categorias_movimiento:
                    categorias_movimiento.append(producto["categoria"])

        for categoria in categorias_movimiento:
            print(categoria)

    else:
        print("no se registraron ventas durante el dia.")
        print("\nPRODUCTOS SIN VENTAS")

        for producto in productos:
            print(producto["nombre"])

        print("no hubo categorias con movimiento.")

