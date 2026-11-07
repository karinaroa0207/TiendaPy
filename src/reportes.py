from datetime import date
from tabulate import tabulate
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
        filas = []

        for producto in productos:
            if producto["proveedor"] == proveedor:
                if producto["stock"] <= producto["stock_minimo"]:
                    if producto["stock"] == 0:
                        estado = "AGOTADO"
                    else:
                        estado = "STOCK BAJO"

                    filas.append([
                        producto["codigo"],
                        producto["nombre"],
                        producto["stock"],
                        producto["stock_minimo"],
                        estado
                    ])

        encabezados = ["Codigo", "Nombre", "Stock actual", "Stock minimo", "Estado"]
        print(tabulate(filas, headers=encabezados, tablefmt="grid"))


def generar_reporte_diario(productos: list) -> None:
    print("\nREPORTE DIARIO")

    ventas = cargar_ventas()
    fecha_actual = date.today().isoformat()

    total_vendido = 0.0
    cantidad_ventas = 0
    productos_vendidos = {}
    categorias_movimiento = []

    for venta in ventas:
        datos = venta.split("|")

        if len(datos) != 3:
            print("se omitio una venta incorrecta.")
            continue

        if datos[0] == fecha_actual:
            try:
                total = float(datos[1])
                if total <= 0:
                    raise ValueError

                detalles = datos[2].split(";")
                temporales = {}

                for detalle in detalles:
                    codigo, cantidad = detalle.split(":")
                    cantidad = int(cantidad)
                    if cantidad <= 0:
                        raise ValueError

                    if codigo not in temporales:
                        temporales[codigo] = 0
                    temporales[codigo] += cantidad

                total_vendido += total
                cantidad_ventas += 1

                for codigo, cantidad in temporales.items():
                    if codigo not in productos_vendidos:
                        productos_vendidos[codigo] = 0
                    productos_vendidos[codigo] += cantidad

            except ValueError:
                print("se omitio una venta incorrecta.")

    if cantidad_ventas > 0:
        promedio = total_vendido / cantidad_ventas

        max_unidades = max(productos_vendidos.values())
        mas_vendidos = []

        for codigo, cant in productos_vendidos.items():
            if cant == max_unidades:
                nombre_prod = codigo
                for producto in productos:
                    if producto["codigo"] == codigo:
                        nombre_prod = producto["nombre"]
                mas_vendidos.append(f"{nombre_prod} ({cant} und)")

        texto_mas_vendido = ", ".join(mas_vendidos)

        tabla_resumen = [
            ["Fecha", fecha_actual],
            ["Total vendido", f"$ {total_vendido}"],
            ["Numero de ventas", cantidad_ventas],
            ["Ticket promedio", f"$ {promedio:.2f}"],
            ["Producto(s) mas vendido(s)", texto_mas_vendido]
        ]
        print(tabulate(tabla_resumen, tablefmt="grid"))

        print("\nPRODUCTOS SIN VENTAS")
        filas_sin_ventas = []
        for producto in productos:
            if producto["codigo"] not in productos_vendidos:
                filas_sin_ventas.append([producto["codigo"], producto["nombre"]])

        if len(filas_sin_ventas) > 0:
            print(tabulate(filas_sin_ventas, headers=["Codigo", "Nombre"], tablefmt="grid"))
        else:
            print("Todos los productos tuvieron ventas hoy.")

        print("\nCATEGORIAS CON MOVIMIENTO")
        filas_categorias = []
        for producto in productos:
            if producto["codigo"] in productos_vendidos:
                if producto["categoria"] not in categorias_movimiento:
                    categorias_movimiento.append(producto["categoria"])
                    filas_categorias.append([producto["categoria"]])

        print(tabulate(filas_categorias, headers=["Categoria"], tablefmt="grid"))

    else:
        tabla_resumen = [
            ["Fecha", fecha_actual],
            ["Total vendido", "$ 0"],
            ["Numero de ventas", 0],
            ["Ticket promedio", "$ 0"],
            ["Producto(s) mas vendido(s)", "ninguno"]
        ]
        print(tabulate(tabla_resumen, tablefmt="grid"))
        print("no se registraron ventas durante el dia.")

        print("\nPRODUCTOS SIN VENTAS")
        filas_sin_ventas = []
        for producto in productos:
            filas_sin_ventas.append([producto["codigo"], producto["nombre"]])

        if len(filas_sin_ventas) > 0:
            print(tabulate(filas_sin_ventas, headers=["Codigo", "Nombre"], tablefmt="grid"))

        print("\nno hubo categorias con movimiento.")