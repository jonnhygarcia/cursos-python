n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa el segundo numero: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numero {n1} y {n2} el resultado seria:
Resultado de la Suma es: {suma}
Resultado de la Resta es: {resta}
Resultado de la multiplicacion es: {multi}
Resultado de la Division es: {div}
"""

print(mensaje)
