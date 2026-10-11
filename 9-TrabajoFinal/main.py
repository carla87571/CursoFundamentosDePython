from menu import mostrar_menu
from pedidos import pedir_cafe

def main():
    while True:
        # Mostrar el menú
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # pedir un café
            pedir_cafe()
        elif opcion == "2":
            # ver el historial de pedidos
            pass
        elif opcion == "3":
            print("\n Muchas gracias por haber tomado nuestros riquísimos cafés")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()