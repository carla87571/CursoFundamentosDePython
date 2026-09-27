v = True
f = False

print(v) # output: True
print(type(v)) # output: <class 'bool'>
print(f) # output: False
print(type(f)) # output: <class 'bool'>

# Boolean operations
print(v and f) # output: False
print(v or f) # output: True
print(not v) # output: False
print(not f) # output: True

# Comparacion de valores
print(5 > 3) # output: True
print(5 < 3) # output: False
print(5 == 5) # output: True
print(5 != 3) # output: True
print(5 >= 3) # output: True
print(5 <= 3) # output: False


# Conversion a booleano
print(bool("Hola Mundo")) # output: True
print(bool("")) # output: False
print(bool(0)) # output: False
print(bool(1)) # output: True

"""
bool() convierte un valor a True o False según si Python lo considera
verdadero o vacío.
Ejemplo:
print(bool("Hola Mundo"))  # True

la cadena no está vacía, se considera True.

print(bool(""))  # False
la cadena está vacía, se considera False.
"""
#Valores booleanos considerados como False:
# None, False, 0, 0.0, "", [], {}, set()

#Todos los demas valores se consideran True 

bool("")       # False
bool(0)        # False
bool(None)     # False
bool([])       # False
bool({})       # False
bool(set())    # False

# Cualquier valor con contenido normalmente devuelve True:

bool("Hola")   # True
bool(25)       # True
bool([1, 2])   # True
bool({1: "a"}) # True
bool({1, 2})   # True

# Aplicación real 
# Por ejemplo, comprobar si un usuario escribió algo:

nombre = input("Escribe tu nombre: ")

if bool(nombre): # Comprobar si el usuario escribió algo
    print(f"Hola, {nombre}")
else:
    print("No escribiste ningún nombre")


# Comprobar el tipo de una variable usando isinstance()
x = 123
print(isinstance(x, int))   # output: True
print(isinstance(x, bool))  # output: False
