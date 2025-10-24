# Alcande de de variables en funciones en Python.
# El alcance de una variable determina dónde puede ser accedida dentro del código. "Variable local" y "variable global" son dos conceptos clave relacionados con el alcance.
# Variable local: Una variable definida dentro de una función. Solo puede ser accedida dentro de esa función.
# Variable global: Una variable definida fuera de cualquier función. Puede ser accedida desde cualquier parte del código, incluidas las funciones.      
saludo = "Hola Global Mundo" # Variable global

def saludo():
    saludo = "Hola Mundo" # Variable local
    print(saludo) # Imprime la variable local 'saludo' dentro de la función.

def saludaChanchito():
    saludo = "Hola Chanchito Feliz" # Variable local
    print(saludo) # Imprime la variable local 'saludo' dentro de la función.

print(saludo) # Error: 'saludo' no está definida en este ámbito global.
saludo() # Llamada a la función saludo(), que define una variable local 'saludo' pero no la devuelve ni la imprime.
saludaChanchito() # Llamada a la función saludaChanchito(), que define una variable local 'saludo' pero no la devuelve ni la imprime.
print(saludo) # Error: 'saludo' no está definida en este ámbito global. 

# Para acceder a las variables locales, debemos hacerlo dentro de sus respectivas funciones.
def saludo():
    saludo = "Hola Mundo" # Variable local
    print(saludo) # Imprime la variable local 'saludo' dentro de la función.        

def saludaChanchito():
    saludo = "Hola Chanchito Feliz" # Variable local
    print(saludo) # Imprime la variable local 'saludo' dentro de la función.    


print(saludo) # Imprime la variable global 'saludo'.
saludo() # Llamada a la función saludo(), que imprime la variable local 'saludo'.
saludaChanchito() # Llamada a la función saludaChanchito(), que imprime la variable local 'saludo'.

# Es Mala practica usar variables globales dentro de funciones, ya que puede llevar a errores difíciles de depurar.
# En su lugar, es preferible pasar las variables como parámetros a las funciones.
def mostrar_saludo(): # La variable 'saludo' es un parámetro de la función.
    global saludo # Declaramos que usaremos la variable global 'saludo_global'.
    saludo = "Hola saludo Global" # Asignamos el valor del parámetro 'saludo' a la variable local 'saludo'.

print("-----")
print(saludo) # Imprime la variable global 'saludo'.    
print(mostrar_saludo) # Llamada a la función mostrar_saludo(), que imprime la variable local 'saludo'.

print("-----")
