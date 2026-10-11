ARCHIVOS_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("/ Elige el café de tu preferencia")
    print("1. Espresso")
    print("2. Cappuccino")
    print("3. Latte")
    print("4. Americano")

    opcion = input("Seleccione una opción: ")

    cafes = {
        "1": "Espresso",
        "2": "Cappuccino",
        "3": "Latte",
        "4": "Americano"
    }

    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print(f"Has pedido un "+ cafe_elegido +". Preparando tu café!...")

        with open(ARCHIVOS_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("Opción no válida, por favor intente de nuevo.")