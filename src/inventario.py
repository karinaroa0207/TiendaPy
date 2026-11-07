from validaciones import pedir_texto
from validaciones import pedir_entero_positivo
from validaciones import pedir_decimal_positivo
from persistencia import guardar_inventario
from tabulate import tabulate

def mostrar_inventario(productos) -> None:
    print("\nINVENTARIO DE TIENDAPY")

    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        filas = []
        for p in productos:
            filas.append([
                p["codigo"], p["nombre"], p["categoria"],
                p["precio"], p["stock"], p["stock_minimo"], p["proveedor"]
            ])
        encabezados = ["Código", "Nombre", "Categoría", "Precio", "Stock", "Stock Mín.", "Proveedor"]
        print(tabulate(filas, headers=encabezados, tablefmt="grid"))
        
def registrar_producto(productos) -> None:
    print("\n---REGISTRAR PRODUCTO---")

    codigo = pedir_texto("Codigo: ").upper()

    for producto in productos:
        if producto["codigo"].upper() == codigo:
            raise ValueError("Ese codigo ya existe.")

    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoria: ")
    precio = pedir_decimal_positivo("Precio: ")
    stock = pedir_entero_positivo("Stock: ")
    stock_minimo = pedir_entero_positivo("Stock minimo: ")
    proveedor = pedir_texto("Proveedor: ")

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "proveedor": proveedor
    }

    productos.append(nuevo_producto)
    guardar_inventario(productos)

    print("\nProducto registrado correctamente.")


def buscar_por_codigo(productos) -> None:
    print("\n--- BUSCAR PRODUCTO POR CODIGO ---")

    codigo = pedir_texto("Ingrese el codigo: ").upper()

    filas = []

    for producto in productos:
        if producto["codigo"].upper() == codigo:
            filas.append([
                producto["codigo"],
                producto["nombre"],
                producto["categoria"],
                producto["precio"],
                producto["stock"],
                producto["proveedor"]
            ])

    if len(filas) == 0:
        print("No se encontro un producto con ese codigo.")
    else:
        print("\nProducto encontrado:")
        encabezados = ["Código", "Nombre", "Categoría", "Precio", "Stock", "Proveedor"]
        print(tabulate(filas, headers=encabezados, tablefmt="grid"))


def buscar_por_categoria(productos) -> None:
    print("\n--- BUSCAR PRODUCTOS POR CATEGORIA ---")

    categoria = pedir_texto("ingrese la categoria: ")

    filas = []

    for producto in productos:
        if producto["categoria"].lower() == categoria.lower():
            filas.append([
                producto["codigo"],
                producto["nombre"],
                producto["precio"],
                producto["stock"]
            ])

    if len(filas) == 0:
        print("no hay productos en esa categoria.")
    else:
        encabezados = ["Código", "Nombre", "Precio", "Stock"]
        print(tabulate(filas, headers=encabezados, tablefmt="grid"))


def modificar_producto(productos) -> None:
    print("\n---MODIFICAR PRODUCTO---")

    codigo = pedir_texto("ingrese el codigo del producto: ").upper()

    encontrado = False

    for producto in productos:
        if producto["codigo"].upper() == codigo:
            encontrado = True

            print("\nproducto encontrado:", producto["nombre"])
            print("1.modificar precio")
            print("2.modificar stock")
            print("3.modificar precio y stock")

            opcion = input("seleccione una opcion: ")

            if opcion == "1":
                producto["precio"] = pedir_decimal_positivo("Nuevo precio: ")

            elif opcion == "2":
                producto["stock"] = pedir_entero_positivo("Nuevo stock: ")

            elif opcion == "3":
                producto["precio"] = pedir_decimal_positivo("Nuevo precio: ")
                producto["stock"] = pedir_entero_positivo("Nuevo stock: ")

            else:
                print("no hay otra opcion")
                return

            guardar_inventario(productos)
            print("producto modificado correctamente.")
            break

    if encontrado == False:
        print("no se encontro el producto.")


def eliminar_producto(productos) -> None:
    print("\n---ELIMINAR PRODUCTO ;)")

    codigo = pedir_texto("ingrese el codigo del producto: ").upper()

    encontrado = False

    for producto in productos:
        if producto["codigo"].upper() == codigo:
            encontrado = True

            print("Producto:", producto["nombre"])
            confirmar = input("desea eliminarlo? (s/n): ").lower()

            if confirmar == "s":
                productos.remove(producto)
                guardar_inventario(productos)
                print("producto eliminado correctamente.")
            else:
                print("no se elimino el producto.")

            break

    if encontrado == False:
        print("no se encontro el producto.")