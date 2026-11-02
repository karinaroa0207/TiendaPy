
from persistencia import cargar_inventario
from inventario import mostrar_inventario, registrar_producto
from inventario import buscar_por_codigo, buscar_por_categoria
from inventario import modificar_producto, eliminar_producto
from ventas import registrar_venta
from reportes import mostrar_alertas_stock
from reportes import generar_reporte_diario

productos = cargar_inventario()

while True:
    print("\nTIENDAPY")
    print("1. mostrar productos")
    print("2. registrar producto")
    print("3. buscar por codigo")
    print("4. buscar por categoria")
    print("5. modificar producto")
    print("6. eliminar producto")
    print("7. registrar venta")
    print("8. alertas de inventario")
    print("9. reporte diario de ventas")
    print("10. salir")

    opcion = input("\nSeleccione una opcion: ")

    if opcion == "1":
        mostrar_inventario(productos)

    elif opcion == "2":
        try:
            registrar_producto(productos)
        except ValueError as error:
            print("no se puede registrar el producto:", error)

    elif opcion == "3":
        buscar_por_codigo(productos)

    elif opcion == "4":
        buscar_por_categoria(productos)

    elif opcion == "5":
        modificar_producto(productos)

    elif opcion == "6":
        eliminar_producto(productos)

    elif opcion == "7":
        try:
            registrar_venta(productos)
        except ValueError as error:
            print("error en la venta:", error)

    elif opcion == "8":
        mostrar_alertas_stock(productos)

    elif opcion == "9":
        generar_reporte_diario(productos)

    elif opcion == "10":
        print("saliendo")
        break

    else:
        print("no sirve")
