# creacion de una calculadora basica con dos numeros enteros con entrada de datos por teclado.
n1 = input("Ingresa el primer número: ")
n2 = input("Ingresa el segundo número: ")

n1 = int(n1)  # Conversión a entero
n2 = int(n2)  # Conversión a entero
# Concatenación, print(n1 + n2) lo que hace es concantenar no suma.
print(n1 + n2)

# creamos la variables de las operaciones.
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

# Creamos una variable con el mensaje a motrar formateado, usando las variables creadas anteriormente.
mensaje = f"""
Para los numeros {n1} y {n2},
El resultado de la suma es {suma}.
El resultado de la resta es {resta}.
El resultado de la multiplicacion es {multi}.
El resultado de la division es {div}.
"""

print(mensaje)
