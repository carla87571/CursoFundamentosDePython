palabra = "Python"

for letra in palabra:
    print(letra)

print("---------------------------------------------------------")

frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    if fruta == "Naranja":
        break
    print(fruta)
print("---------------------------------------------------------")

ftutas2 = ["pera", "kiwi", "mango"]

for fruta in ftutas2:
    if fruta == "kiwi":
        continue
    print(fruta)
else:
    print("Se han recorrido todas las frutas excepto kiwi")

print("---------------------------------------------------------")  
# range
# Comienza desde 0 hasta 9 (10 no incluido)
for i in range(10):
    print(i)

print("----------------------------------------------------------------")    

for i in range(3,5): # inicializa en 3 y termina en 4 (5 no incluido)
    print(i)

print("----------------------------------------------------------------------")

for i in range(2, 10, 2): # inicializa en 2, termina en 8 (10 no incluido), incrementa de 2 en 2
    print(i)
print("-----------------------------------------------------------------------------")    

frutas = ["manzana", "banana", "cereza"]
adjetivos = ["Rica", "Saludable"]


for fruta in frutas:
    for adjetivo in adjetivos:
        print(f"{fruta} {adjetivo}")
print("---------------------------------------------------------")

for i in range(5):
    pass # este marcador de posición indica que no se realiza ninguna acción en este bucle, hasta que decidamos qué hacer con él