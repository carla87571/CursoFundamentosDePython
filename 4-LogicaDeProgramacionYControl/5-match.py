dia = 1
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Día no válido")

"""
Python no sabe por sí mismo que 1 significa lunes. Esa relación la defines tú mediante los case.

El código funciona así:

Supongamos que dia = 1.

El match compara dia con cada case en orden:

- Primero compara con case 1. Como dia es 1, hay coincidencia.
- Ejecuta el bloque de case 1: print("Lunes").
- No revisa los siguientes casos porque ya encontró una coincidencia.



Cuando encuentra una coincidencia, ejecuta ese bloque y no revisa los siguientes casos.

Es equivalente a escribir:

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
# ...
else:
    print("Día no válido")
"""