# Tupla: Colección ordenada e inmutable de elementos, permite valores duplicados

# Indices       0          1          2
tecnologias = ("Python", "JavaScript", "Go", "Pyrhon")

print(tecnologias)  # output: ("Python", "JavaScript", "Go", "Pyrhon")
print(tecnologias[0])  # output: "Python"

print(len(tecnologias))  # output: 4

print(type(tecnologias))  # output: <class 'tuple'>
print("-------------------------------------------------------------")

# Tupla de un solo elemento
fruta = ("Manzana",)  # Nota: para crear una tupla de un solo elemento, se debe incluir la coma 
print(type(fruta))  # output: <class 'tuple'>

print("-------------------------------------------------------------")

# Tupla con diferentes tipos de datos
tupla_mixta = ("Python", 3.8, True)
print(tupla_mixta)  # output: ("Python", 3.8, True)
print(type(tupla_mixta))  # output: <class 'tuple'>
print("-------------------------------------------------------------")

# desempaquetado de tuplas
x, y, z = tupla_mixta
print(x)  # output: "Python"
print(y)  # output: 3.8
print(z)  # output: True
print("-------------------------------------------------------------")

tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)
tupla3 = tupla1 + tupla2 # output: (1, 2, 3, 3, 4, 5)
print(tupla3)  # output: (1, 2, 3, 3, 4, 5)
print("-------------------------------------------------------------")

tupla = ("Python", 5, True)  # tupla con diferentes tipos de datos
tupla2 = tupla * 2 # output: ("Python", 5, True, "Python", 5, True   )
print(tupla2)  # output: ("Python", 5, True, "Python", 5, True)
print(tupla)  # output: ("Python", 5, True)
print("-------------------------------------------------------------")

# for: iterar sobre los elementos de la tupla
for elemento in tupla:
    print(elemento)  # output: "Python", 5, True (en cada iteración)
print("-------------------------------------------------------------")

# truco para modificar una tupla: convertirla en lista, modificarla y luego convertirla de nuevo en tupla

tuplaAModificar = ("Python", "JavaScript", "Go")
listaAModificar = list(tuplaAModificar)
listaAModificar.append("Python")  # ejemplo de modificación
tuplaAModificar = tuple(listaAModificar)  # convertir la lista modificada de nuevo en tupla 
print(tuplaAModificar)  # output: ("Python", "JavaScript", "Go", "Python")


