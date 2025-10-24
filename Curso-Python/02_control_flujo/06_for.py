# el bucle for itera sobre una secuencia (lista, cadena, rango, etc.)
# en cada iteración, la variable toma el valor del siguiente elemento de la secuencia
# y se ejecuta el bloque de código indentado
# el bucle termina cuando se han iterado todos los elementos de la secuencia
# for numero in range(5):
#     print(numero, numero * 'Hola mundo')

# Busca el numero 3 y cunado lo encuentra muestra mensaje "encontrado" y con brake se deteniene la busqueda
buscar = 3 # valor a buscar
for numero in range(5): # itera sobre los números del 0 al 4
    print(numero) # imprime el numero actual en cada iteración
    if numero == buscar: # si el numero es igual al valor de buscar
        print("encontrado", buscar) # muestra mensaje "encontrado" al encontrar el valor buscar.
        break  # sale del bucle al encontrar el valor buscar.
else: # el else se ejecuta si el bucle for termina sin encontrar el valor buscar
    print("no encontrado el numero") 


print("-----")
print("")

# Si no lo encuentra el numero, en el rango indiciado, muestra el mensaje "no encontrado" en este caso no lo encontrará porque
# el rango de busqueda es de 5 y el numero a buscar es el 10
buscar2 = 10
for numero in range(5):
    print(numero)
    if numero == buscar2:
        print("encontrado", buscar2)
        break  # sale del bucle al encontrar el valor buscar.
else:
    print(f"no encontrado el numero {buscar2}")

print("-----")
print("")

# caracteres interables, como listas, tuplas, strings, y diccionarios:
for char in "ultimos en enterarse":  # se intera con cada uno de los caracter.
    print(char)  # imprime cada caracter en una linea diferente
