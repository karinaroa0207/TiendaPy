from datetime import date
from tabulate import tabulate

from validaciones import pedir_texto
from validaciones import pedir_entero_positivo
from validaciones import pedir_decimal_positivo

from persistencia import guardar_inventario
from persistencia import guardar_venta


def buscar_producto(productos: list, codigo: str) -> dict | None:
    for producto in productos:
        if producto["codigo"].upper() == codigo.upper():
            return producto

    return None


def calcular_descuento(subtotal: float) -> float:
    if subtotal >= 100000:
        return subtotal * 0.10
    elif subtotal >= 50000:
        return subtotal * 0.05
    else:
        return 0.0


def registrar_venta(productos: list) -> None:
    print("\n---REGISTRAR VENTA---")

    carrito = []

    while True:
        codigo = input(
            "\ningrese el codigo del producto (0 para terminar): "
        ).strip().upper()

        if codigo == "0":
            break

        producto = buscar_producto(productos, codigo)

        if producto is None:
            print("no existe un producto con ese codigo.")
            continue

        if producto["stock"] == 0:
            print("este producto esta agotado.")
            continue

        cantidad = pedir_entero_positivo("cantidad: ")

        cantidad_carrito = 0

        for item in carrito:
            if item["codigo"] == producto["codigo"]:
                cantidad_carrito = item["cantidad"]

        disponible = producto["stock"] - cantidad_carrito

        if cantidad > disponible:
            raise ValueError("no hay suficiente stock disponible.")

        encontrado = False

        for item in carrito:
            if item["codigo"] == producto["codigo"]:
                item["cantidad"] += cantidad
                encontrado = True

        if encontrado == False:
            carrito.append({
                "codigo": producto["codigo"],
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": cantidad
            })

        print("producto agregado al carrito.")

    if len(carrito) == 0:
        print("la venta no contiene productos.")
        return

    subtotal = 0
    filas_detalle = []

    print("\n---DETALLE DE LA VENTA---")

    for item in carrito:
        valor = item["precio"] * item["cantidad"]
        subtotal += valor
        filas_detalle.append([
            item["nombre"],
            item["cantidad"],
            f"$ {valor}"
        ])

    print(tabulate(filas_detalle, headers=["Producto", "Cantidad", "Valor"], tablefmt="grid"))

    descuento = calcular_descuento(subtotal)
    total = subtotal - descuento

    print("\nSubtotal:", subtotal)
    print("Descuento:", descuento)
    print("Total a pagar:", total)

    pago = pedir_decimal_positivo("ingrese el pago recibido: ")

    while pago < total:
        print("el pago es insuficiente.")
        pago = pedir_decimal_positivo("ingrese nuevamente el pago: ")

    cambio = pago - total

    print("Cambio:", cambio)

    for item in carrito:
        producto = buscar_producto(productos, item["codigo"])
        producto["stock"] -= item["cantidad"]

    guardar_inventario(productos)

    detalle = []

    for item in carrito:
        detalle.append(item["codigo"] + ":" + str(item["cantidad"]))

    registro = (
        date.today().isoformat() + "|" +
        str(total) + "|" +
        ";".join(detalle)
    )

    guardar_venta(registro)

    print("\nventa registrada")