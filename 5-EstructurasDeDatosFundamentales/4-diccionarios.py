# Diccionarios (dict): Colección de pares clave-valor, donde cada clave es única.

auto = {
    "marca": "Renault",
    "modelo" :"Clio",
    "año": 2025
}

# Imprimir el diccionario completo y valores individuales
print(auto) # output: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2025}
print(auto["marca"]) # output: 'Renault'
print(auto["modelo"]) # output: 'Clio'
print(auto["año"]) # output: 2025

# Otra forma de acceder a los valores es usando el método get
print(auto.get("marca")) # output: 'Renault'
print(auto.get("modelo")) # output: 'Clio'
print(auto.get("año")) # output: 2025

# Intentar acceder a una clave que no existe devuelve None en lugar de lanzar un error
print(auto.get("color")) # output: None

# Podemos proporcionar un valor por defecto que se devolverá si la clave no existe
print(auto.get("color", "Desconocido")) # output: 'Desconocido'

# Si quiero obtener todas keys (claves) del diccionario
print(auto.keys()) # output: dict_keys(['marca', 'modelo', 'año'])

# Si quiero obtener todos los valores del diccionario
print(auto.values()) # output: dict_values(['Renault', 'Clio', 2025])

# Verificar si una clave existe en el diccionario
if "marca" in auto: # Verifica si la clave 'marca' existe en el diccionario
    print("La clave 'marca' existe en el diccionario") # output: La clave 'marca' existe en el diccionario
if "color" not in auto: # Verifica si la clave 'color' no existe en el diccionario
    print("La clave 'color' no existe en el diccionario") # output: La clave 'color' no existe en el diccionario

print(auto) # output: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2027, 'color': 'Azul'}

# Iterar sobre las claves del diccionario
for k in auto: # Keys
    print(k) # output: 'marca', 'modelo', 'año', 'color' (cada clave en una línea)

# Iterar sobre los valores del diccionario
for v in auto.values():
    print(v) # output: 'Renault', 'Clio', 2027, 'Azul' (cada valor en una línea)

# Iterar sobre los pares clave-valor del diccionario
for k, v in auto.items():
    print(k, v) # output: 'marca: Renault', 'modelo: Clio', 'año: 2027', 'color: Azul' (cada par en una línea)


# Modificar el valor de una clave existente en el diccionario
auto["año"] = 2026 # Modifica el valor de la clave 'año'
print(auto) # output: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2026}

# Agregar una nueva clave-valor al diccionario
auto["color"] = "Rojo" # Agrega la clave 'color' con el valor 'Rojo'
print(auto) # output: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2026, 'color': 'Rojo'}

# .update: Permite actualizar múltiples claves-valor en el diccionario
auto.update({"año": 2027, "color": "Azul"}) # Actualiza las claves 'año' y 'color'
print(auto) # output: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2027, 'color': 'Azul'}

auto.update({"puertas": 4}) # Agrega la clave 'puertas' con el valor 4
print(auto) # output: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2027, 'color': 'Azul', 'puertas': 4}

# Eliminar una clave-valor del diccionario
auto.pop("puertas") # Elimina la clave 'puertas' y su valor
print(auto) # output: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2027, 'color': 'Azul'}

auto.popitem() # Elimina el último par clave-valor agregado al diccionario
print(auto) # output: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2027}

# Limpiar todos los elementos del diccionario
auto.clear() # Elimina todos los pares clave-valor del diccionario
print(auto) # output: {}    


# Diccionarios anidados: Un diccionario puede contener otros diccionarios como valores

familia = {
    "hijo1": {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2": {
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3": {
        "nombre": "Marcelo",
        "edad": 6
    }
}

print(familia["hijo1"]["nombre"]) # output: 'Pedro'
print(familia["hijo2"]["edad"]) # output: 7
print(familia["hijo3"]["nombre"]) # output: 'Marcelo'