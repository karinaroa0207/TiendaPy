from persistencia import cargar_inventario
from inventario import mostrar_inventario, registrar_producto
from inventario import buscar_por_codigo, buscar_por_categoria

productos = cargar_inventario()

while True:
    print("\n--- MENU DE INVENTARIO ---")
    print("1. Mostrar productos")
    print("2. Registrar producto")
    print("3. Buscar por codigo")
    print("4. Buscar por categoria")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        mostrar_inventario(productos)

    elif opcion == "2":
        registrar_producto(productos)

    elif opcion == "3":
        buscar_por_codigo(productos)

    elif opcion == "4":
        buscar_por_categoria(productos)

    elif opcion == "5":
        print("Saliendo del inventario...")
        break

    else:
        print("Opcion incorrecta.")