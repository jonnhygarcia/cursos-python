# el bucle for itera sobre una secuencia (lista, cadena, rango, etc.)
# en cada iteración, la variable toma el valor del siguiente elemento de la secuencia
# y se ejecuta el bloque de código indentado
# el bucle termina cuando se han iterado todos los elementos de la secuencia
# for numero in range(5):
#     print(numero, numero * 'Hola mundo')

# Busca el numero 3 y cunado lo encuentra muestra mensaje "contrado" y con brake se deteniene la busqueda
buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break  # sale del bucle al encontrar el valor buscar.
else:
    print("no encontrado el numero")

# Si no lo encuentra el numero, en el rango indiciado, muestra el mensaje "no encontrado"
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break  # sale del bucle al encontrar el valor buscar.
else:
    print("no encontrado el numero")

# caracteres interables, como listas, tuplas, strings, y diccionarios:
for char in "ultimos en enterarse":  # se intera con cada caracter.
    print(char)  # imprime cada caracter en una linea diferente
