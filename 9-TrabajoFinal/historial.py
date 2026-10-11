ARCHIVOS_PEDIDOS = "pedidos.txt"

def ver_historial():
    try:
        print("\n Historial de pedidos:")
        with open(ARCHIVOS_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for pedido in pedidos:
                    print(pedido.strip())
            else:
                print("No hay pedidos en el historial.")
    except FileNotFoundError:
        print("No se encontró el historial de pedidos.")