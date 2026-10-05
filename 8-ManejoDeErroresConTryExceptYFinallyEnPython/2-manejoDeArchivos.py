# open(nombre, modo)
# Modos comunes:
# R (read) lectura
# W (write) - escritura (sobrescribe el archivo)
# X (exclusive creation) - crea un archivo nuevo, falla si ya existe


try:
    with open("archivo.txt", "r") as f:
        print(f.readline())
except FileNotFoundError:
    print("El archivo no existe")
