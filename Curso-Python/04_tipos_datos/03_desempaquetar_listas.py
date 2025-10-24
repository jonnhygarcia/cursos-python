numeros = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

# feo y en deshuso
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# Los mas parecidos a los punteros, poner una variable con argumentos ( * ) delante pora englobar una lista dentro de una lista.
# puedes asignar que numeros estan fuera o dentro segun lo que se necesite.
primero, segundo, *otros, ultimo = numeros
print(primero, segundo, otros, ultimo)