# Sintaxis básica de try-except en Python
try:
    print("Intentamos algo que podría fallar")
except:
    print("Captura el error")

print("-----------------------------------------------------------------------")

try:
    numero = 10/0
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")

print("-----------------------------------------------------------------------")

try:
    print(x)
except NameError:
    print("La variable no está definida")
finally:
    print("Esto se ejecuta siempre, haya ocurrido un error o no")

print("-----------------------------------------------------------------------")
