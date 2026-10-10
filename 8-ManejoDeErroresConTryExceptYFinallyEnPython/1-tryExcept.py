# Sintaxis básica de try-except en Python
try:
    print("Intentamos algo que podría fallar")
except:
    print("Captura el error")

print("-----------------------------------------------------------------------")
# Manejo de la división por cero
try:
    numero = 10/0
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")

print("-----------------------------------------------------------------------")
# Manejo de la variable no definida con NameError
try:
    print(x)
except NameError:
    print("La variable no está definida")
finally:
    print("Esto se ejecuta siempre, haya ocurrido un error o no")

print("-----------------------------------------------------------------------")
