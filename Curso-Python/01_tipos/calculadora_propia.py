n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa el segundo numero: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
El resultado de los numeros "{n1} y {n2} son:
la suma seria: {suma}
la resta seria: {resta}
la multiplicacion seria: {multi}
la division seria: {div}
"""

print(mensaje)
