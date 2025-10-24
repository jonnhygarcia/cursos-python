# las tuplas son como las listas pero con el incoveniente que no se pueden modificar para nada.
# Se usan para crear listas, cerradas, que no se puedan modifcar solo cosultar, aunque se puede copiar
# un tupla, convertirla en lista y modificar la misma.

# Las tuplas se diferencia con las lista, que se crean con parentesis "( )" y se pueden anidar sumandolas.
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# con tuple puedes convertir en tupla, cualquier lista, contenta lo que contenga, strings, bools, enteros, etc...
punto = tuple([1, 2])
print(punto)

# acceder a una tupla, accerdemos a un tupla numeros y creamos una nueva tupla a raiz de una liasta menosNumeros
menosNumeros = numeros[:2]
print(menosNumeros)

# tambien podemos desempaquetar una tupla
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# podemos iterar en las tuplas. NO MODIFICARLAS DIRECTAMENTE.
for n in numeros:
    print(n)

# La unica forma de modificar entre comillas una tupla es creando una lista de la misma y modificar esta ultima.    
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito feliz"
print(listaNumeros)