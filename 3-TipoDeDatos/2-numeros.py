x = 1
y = 2.5
z = 4j

print(type(x)) # output: <class 'int'>
print(type(y)) # output: <class 'float'>
print(type(z)) # output: <class 'complex'>

positivo = 5
negativo = -3
print(type(positivo)) # output: <class 'int'>
print(type(negativo)) # output: <class 'int'>

flotante = 3.14
flotanteNegativo = -3.14
print(type(flotante)) # output: <class 'float'>
print(type(flotanteNegativo)) # output: <class 'float'>

complejo = 2 + 3j
complejoNegativo = -2 - 3j
print(type(complejo)) # output: <class 'complex'>
print(type(complejoNegativo)) # output: <class 'complex'>

# Casteo
xf = float(x)
print(type(xf)) # output: <class 'float'>
print(xf) # output: 1.0

ye = int(y)
print(type(ye)) # output: <class 'int'>
print(ye) # output: 2

entero = 5
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print(type(enteroComplejo)) # output: <class 'complex'>
print(type(flotanteComplejo)) # output: <class 'complex'>
print(enteroComplejo) # output: (5+0j)
print(flotanteComplejo) # output: (5.5+0j)

# Números aletorios
import random

print(random.randint(1, 10)) # output: un número aleatorio entre 1 y 10
print(random.randrange(1, 10)) # output: un número aleatorio entre 1 y 9
print(random.random()) # output: un número aleatorio entre 0.0 y 1.0