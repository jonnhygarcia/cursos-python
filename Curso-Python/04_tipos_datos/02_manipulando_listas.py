mascotas = ["wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])

mascotas[0] = "Bicho"
print(mascotas)

# La parte izquierda del arreglo "[ x : ]" es el indice de la pocicion a seleccionar
# La parte derecha del arreglo "[ : x ]" es hasta donde llega la seccion en la lista. 
print(mascotas[2:])

#empieza de derecha a izquierda y muestra el ultimo de la lista.
print(mascotas[-1])

print(mascotas[1:2:2])

# Estos dos puntos dice coge el primer elemento, salta el siguiete, y vulve a cojer el siguiente.
print(mascotas[::2])

# empieza desde el 1 no desde el 0, y va saltando uno recupera el siguiente.
print(mascotas[1::2])

# empieza desde el 1 no desde el 0, y va saltando uno recupera el siguiente, hasta dos elementos en total que seria el 2 de enmedio lo que lo indicaria.
print(mascotas[1:2:2])


numeros = list(range(21))
print(numeros)

#empieza desde el 0 de dos en dos y salen los numeros pares.
print(numeros[::2])

#empieza desde el 1 y te muestra los numeros impares.
print(numeros[1::2])

# de esta forma le pedimos un rango del 1 al 21 no empieza desde el 0
numeros2 = list(range(1, 21))
print(numeros2)

# con lo que aqui se pedia antes pares ahora salen impares al empezar desde el 1 y no desde el 0
print(numeros2[::2])