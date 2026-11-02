from persistencia import cargar_inventario

print("INVENTARIO DE TIENDAPY")

productos = cargar_inventario()

for producto in productos:
    print(producto)