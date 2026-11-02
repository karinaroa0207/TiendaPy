from validaciones import pedir_texto
from validaciones import pedir_entero_positivo
from validaciones import pedir_decimal_positivo
from persistencia import guardar_inventario


def mostrar_inventario(productos):
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


def registrar_producto(productos):
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = pedir_texto("Codigo: ")

    for producto in productos:
        if producto["codigo"] == codigo:
            print("ese codigo ya existe.")
            return

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
    
    
def buscar_por_codigo(productos):
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


def buscar_por_categoria(productos):
    print("\n--- BUSCAR PRODUCTOS POR CATEGORIA ---")

    categoria = pedir_texto("Ingrese la categoria: ")

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
        print("No hay productos en esa categoria.")