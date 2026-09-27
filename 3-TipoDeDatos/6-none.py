"""
Una función devuelve None cuando no encuentra un resultado o cuando solo realiza una acción.

Ejemplo: buscar un usuario
"""

def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            return usuario

    return None  # No se encontró el usuario


usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30}
]

resultado = buscar_usuario(usuarios, "Carlos")

if resultado is None:
    print("El usuario no existe")
else:
    print(f"Usuario encontrado: {resultado}")






# None es la ausencia de valor en Python
x = None
print(x) # output: None
print(type(x)) # output: <class 'NoneType'>

# Comprobar si una variable es None
if x is None:
    print("x es None")
else:
    print("x no es None")

print(type("")) # output: <class 'str'>
print(type(0)) # output: <class 'int'>
print(type(False)) # output: <class 'bool'>
print(type([])) # output: <class 'list'>
print(type({})) # output: <class 'dict'>
print(type(set())) # output: <class 'set'>
print(type(None)) # output: <class 'NoneType'>

