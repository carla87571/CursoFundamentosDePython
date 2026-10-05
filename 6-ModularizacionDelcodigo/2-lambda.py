# Lambda es una función pequeña y anónima que puede tener muchos argumentos pero sólo una expresión.
# Sintaxis: lambda argumentos : expresión

x = lambda a, b : a + b
print(x(5, 3))  # output: 8


def miFuncion(n):
    return lambda a : a * n

duplicador = miFuncion(2)
print(duplicador(5))  # output: 10

triplicador = miFuncion(3)
print(triplicador(5))  # output: 15

'''
una lambda es una forma compacta de crear una función pequeña, 
pero no es solo “reducir código”. Tiene una limitación importante:
 su cuerpo contiene una sola expresión, cuyo resultado se devuelve automáticamente.

sumar = lambda a, b: a + b
print(sumar(5, 3))  # 8

Es equivalente a:
def sumar(a, b):
    return a + b

print(sumar(5, 3))  # 8
------------------------------------------------------------------
Las lambdas se usan sobre todo cuando necesitas una función breve en un lugar puntual,
por ejemplo como criterio de ordenación:

personas = [("Ana", 30), ("Luis", 22)]
ordenadas = sorted(personas, key=lambda persona: persona[1])
print(ordenadas)  # output: [('Luis', 22), ('Ana', 30)]
Aquí key recibe una función que extrae la edad de cada persona. Para funciones con nombres,
 varios pasos o lógica compleja, suele ser más claro usar def
'''

personas = [("Ana", 30), ("Luis", 22)]
ordenadas = sorted(personas, key=lambda persona: persona[1])
print(ordenadas)  # output: [('Luis', 22), ('Ana', 30)]
