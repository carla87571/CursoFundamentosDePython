x = 5
y = 3
z = 1

if x > y or x < z:
    print("5 es mayor que 3 o 5 es menor que 1") # V or F entonces es True
if y <  x and y > z:
    print("3 es menor que 5 y mayor que 1")
elif x == y:
    print("5 es igual a 3")
else:
    print("Ninguna de las condiciones se cumple")

print("-----------------------------------------------------------------------------")


a = "Python"
b = "JavaScript"
c = "Python"

if a == c:
    if a != b:
        print("Python es igual a Python y Python es diferente a JavaScript")
    else:
        print("no se cumple la condición")
else:
    print("Ninguna de las condiciones se cumple")

print("-----------------------------------------------------------------------------")

e = 10
f = 10

if e == f:
    pass # Para ignorar la estructura if hasta que definamos que comportamiento se espera
