# Conjuntos (set): Colección no ordenada de elementos únicos (no se puede acceder por índice)

frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
print(frutas) # {'Manzana', 'Naranja', 'Mandarina'}
print(type(frutas)) # output: <class 'set'
print(len(frutas)) #3

print("Manzana" in frutas)
print("Pera" not in frutas)

#Agregar elementos al conjunto
# Agregar con add
frutas.add("Pera") # output  {'Pera','Manzana', 'Naranja', 'Mandarina'}
print(frutas)

# Update
frutasTropicales = {"Piña", "Mango"}
frutas.update(frutasTropicales) # output {'Manzana', 'Naranja', 'Mandarina', 'Pera', 'Piña', 'Mango'}
print(frutas)

# Eliminar elementos del conjunto
# remove: Elimina un elemento del conjunto. Si el elemento no existe, lanza un KeyError.
frutas.remove("Pera") # output {'Manzana', 'Naranja', 'Mandarina', 'Piña', 'Mango'}
print(frutas)

# discard: Elimina un elemento del conjunto. Si el elemento no existe, no lanza error.
frutas.discard("Mango") # output {'Manzana', 'Naranja', 'Mandarina', 'Piña'}
print(frutas)

# pop : Elimina un elemento aleatorio del conjunto
frutas.pop() # Elimina elemento aleatorio del conjunto
print(frutas) # output: {'Manzana', 'Naranja', 'Mandarina', 'Piña'} (el elemento eliminado puede variar)

# clear
frutas.clear() # Elimina todos los elementos del conjunto
print(frutas) # output: set()
print("-------------------------------------------------------------------")

# Conjuntos pueden contener diferentes tipos de datos
conjuntos = {"Python", 156, True}
print(conjuntos)
print (type(conjuntos))

# En los conjuntos cuando los recorremos, el output No lo imprime ordenado igual 
# que el orden al asignar la variable.
for item in conjuntos:
    print(item)

print("-------------------------------------------------------------------")

a = {"a", "b", "c"}
b = {"c", "d", "e"}

# Operaciones con conjuntos
# Unión: no incluye elementos duplicados, combina todos los elementos de ambos conjuntos
union = a | b
c = a.union(b) # output {'a', 'b', 'c', 'd', 'e'}
print(union) # output: {'a', 'b', 'c', 'd', 'e'}

# Intersección: devuelve un conjunto con los elementos que están en ambos conjuntos
c = a.intersection(b) # output {'c'}
interseccion = a & b
print(interseccion) # output: {'c'}

# Diferencia: devuelve un conjunto con los elementos que están en el primer conjunto pero no en el segundo
c = a.difference(b) # output {'a', 'b'}
diferencia = a - b
print(diferencia) # output: {'a', 'b'}

# Diferencia simétrica: devuelve un conjunto con los elementos que están en uno u otro conjunto, pero no en ambos
diferencia_simetrica = a ^ b
print(diferencia_simetrica) # output: {'a', 'b', 'd', 'e'}