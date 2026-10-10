# open(nombre, modo)
# Modos comunes:
# R (read) lectura
# W (write) - escritura (sobrescribe el archivo)
# X (exclusive creation) - crea un archivo nuevo, falla si ya existe


try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    print("No se encontró el archivo")
finally:
    print("Se intentó abrir el archivo")
    

try:
    with open("archivo.txt", "w", encoding="utf-8") as f:
        f.write("Hola Mundo desde el write\n")
        
except FileNotFoundError:
    print("No se encontró el archivo")
finally:
    print("Se intentó escribir en el archivo")


try:
    with open("archivo.txt", "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("Hola Mundo desde el append\n")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No se encontró el archivo")