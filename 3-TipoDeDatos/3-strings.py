print("Hola 'mundo'")

# Crear un string con comillas simples dentro
ingles = "I´m a student"
print(ingles) # output: I'm a student
# Crear un string con múltiples líneas
multiples = """Hola
mundo"""
print(multiples) 

# Contar la cantidad de caracteres en una palabra
palabra = "Murciélago"
print(len(palabra)) # output: 10

# Saber si una palabra contiene una letra específica
texto = "Este curso es de Fundamentos de Python"
estaIncluida = "Python" in texto
noEstaIncluida = "JavaScript" not in texto

print(noEstaIncluida) # output: True
print(estaIncluida) # output: True

# Cambiar Strings a Mayúsculas y Minúsculas
textoMayusculas = texto.upper()
print(textoMayusculas) # output: ESTE CURSO ES DE FUNDAMENTOS DE PYTHON
textoMinusculas = texto.lower()
print(textoMinusculas) # output: este curso es de fundamentos de python

# Saber si una palabra contiene una letra específica (no incluida)
estaIncluida = "Java" in texto
print(estaIncluida) # output: False

# Eliminar espacios al inicio y al final de un string
espacios = "   Hola mundo   "

sin_espacios = espacios.strip()
print(sin_espacios) # output: "Hola mundo"

sin_espacios_alComienzo = espacios.lstrip()
print(sin_espacios_alComienzo) # output: "Hola mundo   "

sin_espacios_alFinal = espacios.rstrip()
print(sin_espacios_alFinal) # output: "   Hola mundo"