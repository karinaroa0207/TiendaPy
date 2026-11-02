def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato == "":
            print("este campo no puede estar vacio.")
        else:
            return dato


def pedir_entero_positivo(mensaje):
    while True:
        try:
            dato = int(input(mensaje))

            if dato <= 0:
                print("debes ingresar un numero mayor que cero.")
            else:
                return dato

        except ValueError:
            print("debes ingresar un numero entero.")


def pedir_decimal_positivo(mensaje):
    while True:
        try:
            dato = float(input(mensaje))

            if dato <= 0:
                print("debes ingresar un valor mayor que cero.")
            else:
                return dato

        except ValueError:
            print("debes ingresar un numero valido.")