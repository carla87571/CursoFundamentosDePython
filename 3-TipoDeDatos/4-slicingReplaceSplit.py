# ind    0123456789101112131415
texto = "Este es un texto"
# Slicing
print(texto[0:4]) # output: Este
print(texto[5:7]) # output: es
print(texto[:]) # output: Este es un texto
print("-----------------------")
print(texto[0:15]) # output: Este es un text
print("-----------------------")
print(texto[:4]) # output: Este
print(texto[8:]) # output: un texto
# indice negativo, cuenta desde el final
print(texto[-5:]) # output: texto
print(texto[::2]) # output: Et s ntxo

# length of the string
print(len(texto)) # output: 17



curso = "Este es un curso de JavaScript"

# Replace "JavaScript" with "Python" in the string
print(curso.replace("JavaScript", "Python")) # output: Este es un curso de Python

# Split divide el string en una lista de palabras
textoDividido = texto.split()
print(textoDividido) # output: ['Este', 'es', 'un', 'texto']


# Normalización
texto2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontarr ciertas palabras"

print("mayusculas" in texto2) # output: False
print("mayusculas" in texto2.lower()) # output: True
print("ciertas" in texto2) # output: True
print("CIERTAS" in texto2) # output: False
print("ciertas" in texto2.lower()) # output: True
