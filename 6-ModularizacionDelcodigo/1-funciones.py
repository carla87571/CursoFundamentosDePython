# Funciones: es un Bloque de código que solo se ejecuta cuando la llamamos.
# Permite organizar y modularizar el código (reutilizable y más legible)

def saludar(nombre, apellido="", nacionalidad= "Colombia"): # argumentos
    print(f"Hola, {nombre} {apellido} de {nacionalidad}")

saludar("Pedro", "Sanchez") # Parametros
saludar("Ana", "Lopez")
saludar("Carlos") # Llamada sin el argumento opcional, usará el valor por defecto ""
saludar("Luis", "Martinez", "Argentina") # Llamada con todos los argumentos especificados

print("-------------------------------------------------------------------------")

def sumar(a, b): # argumentos
    return a + b
print("-------------------------------------------------------------------------")
resultado = sumar(3, 5)
print(f"El resultado de la suma es: {resultado}")


def funcion():
    pass