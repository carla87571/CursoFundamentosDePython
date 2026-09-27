# Strings
comillasSimple = 'Este es un texto'
comillasDoble = "Este es un texto"
comillasTriples = '''comillas triples'''
print(comillasSimple)
print(comillasDoble)
print(comillasTriples)

# Números
a = 1
print(a) # output 1

b = 3.14
print(b) # output 3.14

c = 2 + 3j
print(c)

#Listas es una colección de elementos ordenados, es mutable y tiene índices.

miLista = [1, 2, 3, 4, 5]
print(miLista)
print(miLista[0])  # Primer elemento imprime 1
print(miLista[-1]) # Último elemento imprime 5

# Tupla es inmutable y tiene elementos ordenados y tiene índices

tupla = ("a", "b", "c")
print(tupla)
print(tupla[0])  # Primer elemento imprime "a"
print(tupla[-1]) # Último elemento imprime "c"

# Diccionario es mutable y tiene elementos desordenados y se accede mediante claves

miDiccionario = {
    "nombre": "Juan", 
    "edad": 30,
    "ciudad": "Madrid"
}
print(miDiccionario)
print(miDiccionario["nombre"])  # Accede al valor asociado a la clave "nombre"
print(miDiccionario.get("edad")) # Accede al valor asociado a la clave "edad"


# Conjuntos es mutable y no tiene elementos ordenados ni índices

miConjunto = {1, 1, 2, 2, 3, 4, 4, 5}
print(miConjunto) # Imprime el conjunto sin elementos duplicados Output {1, 2, 3, 4, 5}
print(3 in miConjunto)  # Verifica si el elemento 3 está en el conjunto (True)

# Booleanos representan valores de verdad: True o False

booleanoVerdadero = True
booleanoFalso = False
print(booleanoVerdadero)
print(booleanoFalso)