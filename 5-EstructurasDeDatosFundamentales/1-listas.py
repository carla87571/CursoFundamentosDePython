
# LISTAS : las listas son ordenadas, modificables y permiten valores duplicados

# Indices       0          1          2          3
frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]
print(frutas)
print(type(frutas)) ## <class 'list'>

# inprimir segundo elemento de la lista
print(frutas[1])  # output: "Naranja"
print("---------------------------------------------------------")

# reasignar el segundo elemento de la lista
frutas[1] = "Plátano"
print(frutas)  # output: ["Manzana", "Plátano", "Mandarina"]
print("---------------------------------------------------------")

# distintos elementos de la lista
lista = ["Carla", 5, True]
print(lista)  # output: ["Carla", 5, True]
print(type(lista)) ## <class 'list'>
print("---------------------------------------------------------")

# Saber cuantos elementos tiene la lista
print(len(frutas))  # output: 4
print(len(lista))  # output: 3
print("---------------------------------------------------------")

# Slicing: obtener una sublista a partir de la lista original
sublista = frutas[1:3]
print(sublista)  # output: ["Plátano", "Mandarina"]

print(frutas[1:])  # output: ["Plátano", "Mandarina", "Naranja"]
print(frutas[:3])  # output: ["Manzana", "Plátano", "Mandarina"]
print("---------------------------------------------------------")

# si un elemento existe en la lista
if "Plátano" in frutas:
    print("Plátano está en la lista de frutas") # output: "Plátano está en la lista de frutas"
print("---------------------------------------------------------")  


# Métodos para poder modificar la lista
vehiculos = ["Auto", "Moto", "Avión"]

# Agregar un elemento al final de la lista
vehiculos.append("Bicicleta")
print(vehiculos)  # output: ["Auto", "Moto", "Avión", "Bicicleta"]

# Insertar un elemento en una posición específica
vehiculos.insert(1, "Camión")
print(vehiculos)  # output: ["Auto", "Camión", "Moto", "Avión", "Bicicleta"]

# Eliminar un elemento por su valor
vehiculos.remove("Moto")
print(vehiculos)  # output: ["Auto", "Camión", "Avión", "Bicicleta"]

# Eliminar un elemento por su índice
del vehiculos[2]
print(vehiculos)  # output: ["Auto", "Camión", "Bicicleta"]

# Vaciar la lista
vehiculos.clear()
print(vehiculos)  # output: []  

# Insertar un elemento en una posición específica
vehiculos.insert(0, "Tren") # output: ["Tren"]
vehiculos.insert(1, "Avión") # output: ["Tren", "Avión"]
vehiculos.insert(2, "Barco") # output: ["Tren", "Avión", "Barco"]

# Pop: eliminar y devolver el último elemento de la lista
ultimo_elemento = vehiculos.pop()
print(ultimo_elemento)  # output: "Barco"
print(vehiculos)  # output: ["Tren", "Avión"]

vehiculos.pop(0) # elimina Tren indice 0 y solo deja ["Avión"]
print(vehiculos)  # output: ["Avión"]

# sort: ordenar la lista
vehiculos.append("Avión") # agrega "Avión" al final de la lista
vehiculos.append("Moto") # agrega "Moto" al final de la lista
vehiculos.append("Auto") # agrega "Auto" al final de la lista
vehiculos.sort() # ordena la lista alfabéticamente
print(vehiculos)  # output: ["Auto", "Avión", "Moto"]
print("-------------------------------------------------------------")

# reverse: invertir el orden de la lista
vehiculos.reverse() # invierte el orden de la lista, output: ["Moto", "Avión", "Auto"]
print("----------------------------------------------------------------------")

# Unir listas (No elimina los elementos duplicados)
coleccion1 = [1, 2, 3]
coleccion2 = [3, 4, 5]

coleccion3 = coleccion1 + coleccion2
print(coleccion3)  # output: [1, 2, 3, 3, 4, 5]

# Otra forma de unir listas es usando el método extend
coleccion1.extend(coleccion2)
print(coleccion1)  # output: [1, 2, 3, 3, 4, 5]



