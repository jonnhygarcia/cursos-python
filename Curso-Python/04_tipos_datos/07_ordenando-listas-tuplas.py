numeros = [2, 4, 1, 45, 75, 22]
numeros2 = [2, 4, 1, 45, 75, 22]
numeros3 = [2, 4, 1, 45, 75, 22]

# numeros.sort()
# numeros2.sort(reverse=True)

# print(numeros)
# print(numeros2)

# Sorted te lo ordena pero creando una lista nueva.
numeros2 = sorted(numeros)
numeros3 = sorted(numeros, reverse=True)
print(numeros) # la lista de numeros normal
print(numeros2) # Nueva lista de numeros creada de cero, nueva, no modificada.
print(numeros3) # Nueva lista al reves, de numeros creada de cero, nueva, no modificada.

print(" ")
print("----")
print(" ")

# con Sort te ordena una lista dentro de una lista, con el id al principio, pero con el id al final o en diferentes orden NO.
# temabien podrias indicar en sort, algun indice o argumentos, pero no deja de limitarse en el orden de indices al inicio.
usuarios = [
    [1, "Chanchito"], 
    [4, "Felipe"], 
    [2, "Pulga"]
]

usuarios.sort()
print(usuarios)

print(" ")
print("----")
print(" ")

usuarios = [
    ["Chanchito", 1], 
    ["Felipe", 4], 
    ["Pulga", 2]
]

# En esta ocacion se crea una funcion que devuelve un indice a los elementos con el 1
def ordena(elemento):
    return elemento[1]

# Al meter el parametro es obligatorio poner "key=xxxxx" para que te ordene la funcion anterior creada.
# asi te da un key o id mas el valor en este caso la ejecucion de la funcion.
# la funcion ordena(), se le paso sin los " ( ) ", porque no queremos pasarle parametros, sino que sort haga el trabajo
# de pasarle los elementos ordenados correspondientes.
usuarios.sort(key=ordena)
print(usuarios)

# Al meter el parametro es obligatorio poner "key=xxxxx" para que te ordene la funcion anterior creada.
# asi te da un key o id mas el valor en este caso la ejecucion de la funcion. Pero en este caso al reves.
usuarios.sort(key=ordena, reverse=True)
print(usuarios)

print(" ")
print("----")
print(" ")

# Con  las funciones Lambda o anonimas, no ahorramos definirla "def", el nombre de la funcion, los parentisis, y el return, con lo que creamos una funcion con pocas palabras en una sola linea, aunque no se recomienda usarla para todo sin para cosas puntuales, que se pueda resolver rapido con esta pequeña funcion. " ¡Sobre todo para funciones de un solo uso!."
print(">> Funcion Lambda : ")
usuarios.sort(key=lambda el:el[1], reverse=True)
print(usuarios)

