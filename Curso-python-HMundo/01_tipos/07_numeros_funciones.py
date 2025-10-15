# Funciones numericas, algunas estan integradas y otras en el modulo math, que mejoran su uso
# https://docs.python.org/3/library/math.html
import math

print(round(2.4))  # Redondea al entero mas cercano
print(round(-2.5))  # redondea al entero mas cercano
print(abs(-77))  # numero negativo a positivo
print(abs(55))  # numero positivo a positivo
print(pow(3, 2))  # Potencia

print(math.ceil(1.1))  # Redondea al entero mayor mas cercano
print(math.floor(1.9999))  # Redondea al entero menor mas cercano
# Comprueba si es un numero no es un numero (NaN) (Not a Number) devuelve False
# Devuelve False si es un numero y True si no lo es como 0/0
print(math.isnan(888))

# Devuelve False si es un numero y True si no lo es como 0/0
print(math.isnan(float('nan')))  # Not a Number, por eso da true.

# Potencia con decimal, indica donde poner el punto decimal o coma.
print(math.pow(10, 3))
print(math.sqrt(9))  # Raiz cuadrada
