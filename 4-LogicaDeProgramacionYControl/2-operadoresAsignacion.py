# Operadores de asignación en Python

x = 5
x += 3  # Equivalente a x = x + 3 output: 8
x *= 4  # Equivalente a x = x * 4 output: 32
x /= 2  # Equivalente a x = x / 2 output: 16.0
x //= 3  # Equivalente a x = x // 3 output: 5.0
x %= 2  # Equivalente a x = x % 2 output: 1.0
x **= 2  # Equivalente a x = x ** 2 output: 1.0


y = 20

y //= 2  # Equivalente a y = y // 2 output: 10
print(y)  # output: 10
y %= 3  # Equivalente a y = y % 3 output: 1
print(y)  # output: 1
y **= 2  # Equivalente a y = y ** 2 output: 1
print(y)  # output: 1

# WALRUS (morsa) :=
# Permite asignar un valor a una variable como parte de una expresión

print(z := 3) # es equivalente a z = 3, es decir, asigna 3 a z 
print(z)  # output: 3

if (n := len("Hola")) > 3:
    print(n)  # output: 4