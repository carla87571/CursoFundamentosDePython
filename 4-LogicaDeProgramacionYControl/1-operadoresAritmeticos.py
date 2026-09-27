# Operadores aritméticos en Python

x = 5
y = 10

# Suma
print(x + y)  # output: 15

# Resta
print(x - y)  # output: -5

# Multiplicación
print(x * y)  # output: 50

# División siempre da un número de punto flotante
print(x / y)  # output: 0.5

# División entera, devuelve el cociente sin el residuo, redondeado al entero más cercano hacia abajo
print(x // y)  # output: 0
print(y // x)  # output: 2

# Módulo, es el residuo de la división
print(x % y)  # output: 5
print(y % x)  # output: 0

# Exponenciación
print(x ** y)  # output: 9765625

# Operaciones

par = 8
print(par % 2 == 0)  # output: True, porque 8 es par

impar = 7
print(impar % 2 != 0)  # output: True, porque 7 es impar

# Predencia de operadores

# Parentesis
# Exponenentes
# Multiplicación, divisiones, divisiones enteras y restos
# Suma y resta
# Comparaciones de identidad y pertenencia
# Operadores lógicos (and, or, not)
# Asignación ( =, +=, -=, *=, /=, //=, %=, **= )
