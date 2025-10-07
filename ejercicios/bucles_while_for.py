"""Bucles while"""
# Bucle while se usa para repetir un bloque de codigo mientras una condicion sea verdadera.

# contador = 0
# while contador < 5:
#    print(f"Iteracion {contador}")
#    contador += 1

# Con el bucle while obligas una y otra vez hasta que le de a Salir o la condicion que se cumpla.    
# respuesta = ""
# while respuesta != "salir":
#    respuesta = input("Escribe algo (o 'salir' para terminar): ")
#    print(f"Dijiste: {respuesta}")
    
"""Bubles for"""
# Bucle for se usa para iterar sobre una secuencia (lista, tupla, cadenas, rangos, etc.)
for numero in range(5):
    print(f"numero: {numero}")

# Ejemplo con listas, genera un imput por cada elemento de la lista.
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta la fruta: {fruta}")
    
    
#Ejemplo de bucle anidado
for i in range(3): # itera 3 veces
    for j in range(2): # itera 2 veces por cada interacion de i
        print(f"i: {i}, j: {j}")
        
# Ejemplo de continue 
for numero in range(5):
    if numero == 3:
        continue
    print(f"numero: {numero}")
    
# Ejemplo de breake 
for numero in range(10):
    if numero == 5:
        break
    print(numero)

# Ejemplo de breake con un else final
for numero in range(5):
    if numero == 6:
        break
else:
    print("el bucle termino y se interrumpio")

# Calculo de Factorial con while
numero = 5
factorial = 1
while numero > 0:
    factorial *= numero
    numero -= 1
print(f"El factorial es: {factorial}")

# creamos tabla de multiplicar al darle un rago de numeros del 1 al 10 y multiplicandolo por el 3.
numero = 3
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# marcador pass, por si aun un codigo o bucle no esta terminado y quieres que sigua funcionando sin errores mientras decides como continuarlo en esa parte, y puedes seguir con el resto del codigo, muy util.
for i in range(5):
    pass  # Aqui puedes implementar la logica mas tarde
else: # se evita mensaje de error, y dar mensaje de "estamos en obras" o segurir con el resto de codigo/bucle.
    print("Bucle terminado, pero la logica no esta implementada aun.") 
