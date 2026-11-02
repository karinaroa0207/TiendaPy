from validaciones import pedir_texto
from validaciones import pedir_entero_positivo
from validaciones import pedir_decimal_positivo
from persistencia import guardar_inventario


def mostrar_inventario(productos) -> None:
    print("\n--- INVENTARIO DE TIENDAPY ---")

    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for producto in productos:
            print("Codigo:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Categoria:", producto["categoria"])
            print("Precio:", producto["precio"])
            print("Stock:", producto["stock"])
            print("Stock minimo:", producto["stock_minimo"])
            print("Proveedor:", producto["proveedor"])


def registrar_producto(productos) -> None:
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = pedir_texto("Codigo: ")

    for producto in productos:
        if producto["codigo"] == codigo:
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

    codigo = pedir_texto("Ingrese el codigo: ")

    encontrado = False

    for producto in productos:
        if producto["codigo"] == codigo:
            print("\nProducto encontrado:")
            print("Nombre:", producto["nombre"])
            print("Categoria:", producto["categoria"])
            print("Precio:", producto["precio"])
            print("Stock:", producto["stock"])
            print("Proveedor:", producto["proveedor"])
            encontrado = True

    if encontrado == False:
        print("No se encontro un producto con ese codigo.")


def buscar_por_categoria(productos) -> None:
    print("\n--- BUSCAR PRODUCTOS POR CATEGORIA ---")

    categoria = pedir_texto("ingrese la categoria: ")

    encontrado = False

    for producto in productos:
        if producto["categoria"].lower() == categoria.lower():
            print("-------------------------")
            print("Codigo:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Precio:", producto["precio"])
            print("Stock:", producto["stock"])
            encontrado = True

    if encontrado == False:
        print("no hay productos en esa categoria.")
        

def modificar_producto(productos) -> None:
    print("\n---MODIFICAR PRODUCTO---")

    codigo = pedir_texto("ingrese el codigo del producto: ")

    encontrado = False

    for producto in productos:
        if producto["codigo"] == codigo:
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

    codigo = pedir_texto("ingrese el codigo del producto: ")

    encontrado = False

    for producto in productos:
        if producto["codigo"] == codigo:
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