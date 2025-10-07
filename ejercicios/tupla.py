# Las tuplas no pueden modificarse una vez creadas (son inmutables).
# Se definen usando paréntesis () y pueden contener elementos de diferentes tipos de datos.
# Se usan para almacenar colecciones de datos que no deben cambiar durante la ejecución del programa.
mi_tupla = (1, "Hola", 3.14, True)
print(mi_tupla[1])  # Salida: (1, 3.14, 'Hola', True)
print(len(mi_tupla))  # Salida: 4 # Longitud de la tupla
# Desempaquetado de tuplas
a, b, c, d = mi_tupla
print(a)  # Salida: 1
print(b)  # Salida: Hola
# Tuplas anidadas
tupla_anidada = (1, (2, 3), (4, 5))
print(tupla_anidada[1][0])  # Salida: 2
# Concatenación de tuplas
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Salida: (1, 2, 3, 4)

# Operaciones con tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
# Suma de tuplas (concatenación)
tupla_suma = tupla1 + tupla2
print(tupla_suma)  # Salida: (1, 2, 3, 4, 5, 6)
# Repetición de tuplas
tupla_repetida = tupla1 * 2
print(tupla_repetida)  # Salida: (1, 2, 3, 1, 2, 3)
# Verificar pertenencia
print(2 in tupla1)  # Salida: True
print(5 not in tupla1)  # Salida: True

#conteo y busqueda en tuplas
mi_tupla = (1, 2, 3, 2, 4, 2)
print(mi_tupla.count(2))  # Salida: 3 # Cuenta cuántas veces aparece el 2
print(mi_tupla.index(3))  # Salida: 2 # Devuelve el índice de la primera aparición del 3
# Si el elemento no existe, index() lanza un error. Para evitarlo, puedes usar una verificación previa:
if 5 in mi_tupla:
    print(mi_tupla.index(5))
else:
    print("El elemento no está en la tupla")  # Salida: El elemento no está en la tupla
# Iterar sobre una tupla
for elemento in mi_tupla:
    print(elemento)
# Salida:
# 1
# 2
# 3

""" 
DIFERENCIAS ENTRE LISTAS Y TUPLAS: 
> Las listas son mutables, las tuplas son inmutables.
> Lista mutable: puedes cambiar, añadir o eliminar elementos.
> Tupla inmutable: no se puede modificar una vez creada. 
"""

# Lista (puedo modificarla)
frutas = ["manzana", "pera", "uva"]
frutas.append("plátano")
print(frutas)  # ['manzana', 'pera', 'uva', 'plátano']

# Tupla (no se puede modificar)
coordenadas = (10, 20)
# coordenadas[0] = 5  # Error


