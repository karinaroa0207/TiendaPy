
from persistencia import cargar_inventario
from inventario import mostrar_inventario, registrar_producto
from inventario import buscar_por_codigo, buscar_por_categoria
from inventario import modificar_producto, eliminar_producto
from ventas import registrar_venta


productos = cargar_inventario()

while True:
    print("\nTIENDAPY")
    print("1. Mostrar productos")
    print("2. Registrar producto")
    print("3. Buscar por codigo")
    print("4. Buscar por categoria")
    print("5. Modificar producto")
    print("6. Eliminar producto")
    print("7. Registrar venta")
    print("8. Salir")

    opcion = input("\nSeleccione una opcion: ")

    if opcion == "1":
        mostrar_inventario(productos)

    elif opcion == "2":
        registrar_producto(productos)

    elif opcion == "3":
        buscar_por_codigo(productos)

    elif opcion == "4":
        buscar_por_categoria(productos)

    elif opcion == "5":
        modificar_producto(productos)

    elif opcion == "6":
        eliminar_producto(productos)

    elif opcion == "7":
        registrar_venta(productos)

    elif opcion == "8":
        print("saliendo")
        break

    else:
        print("no sirve")
