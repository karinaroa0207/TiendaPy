import os

RUTA_INVENTARIO = "data/inventario.txt"
RUTA_VENTAS = "data/ventas.txt"


def cargar_inventario() -> list:
    productos = []

    if not os.path.exists(RUTA_INVENTARIO):
        print("No se encontro el archivo de inventario.")
        return productos

    try:
        with open(RUTA_INVENTARIO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")

                if len(datos) == 7:
                    producto = {
                        "codigo": datos[0],
                        "nombre": datos[1],
                        "categoria": datos[2],
                        "precio": float(datos[3]),
                        "stock": int(datos[4]),
                        "stock_minimo": int(datos[5]),
                        "proveedor": datos[6]
                    }

                    productos.append(producto)
                else:
                    print("Advertencia: se omitio una linea incorrecta.")

    except (ValueError, OSError) as error:
        print("Error al leer el inventario:", error)

    return productos


def guardar_inventario(productos) -> None:
    try:
        with open(RUTA_INVENTARIO, "w", encoding="utf-8") as archivo:
            for producto in productos:
                linea = (
                    producto["codigo"] + "|" +
                    producto["nombre"] + "|" +
                    producto["categoria"] + "|" +
                    str(producto["precio"]) + "|" +
                    str(producto["stock"]) + "|" +
                    str(producto["stock_minimo"]) + "|" +
                    producto["proveedor"] + "\n"
                )

                archivo.write(linea)

    except OSError as error:
        print("Error al guardar el inventario:", error)


def guardar_venta(venta) -> None:
    try:
        with open(RUTA_VENTAS, "a", encoding="utf-8") as archivo:
            archivo.write(venta + "\n")

    except OSError as error:
        print("Error al guardar la venta:", error)


def cargar_ventas() -> list:
    ventas = []

    if not os.path.exists(RUTA_VENTAS):
        return ventas

    try:
        with open(RUTA_VENTAS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip() != "":
                    ventas.append(linea.strip())

    except OSError as error:
        print("Error al leer las ventas:", error)

    return ventas