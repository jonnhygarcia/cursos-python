# Definicion y llamada a funciones en Python
# Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica.
# Se define utilizando la palabra clave 'def', seguida del nombre de la funcion y parentesis.
# Los parametros son variables que se pasan a la funcion para que pueda trabajar con diferentes datos.
# Los argumentos son los valores reales que se pasan a la funcion cuando se llama, valores de los parametros.

# Ejemplo sin parametro.
def hola(): # Definicion de la funcion
    print("Hola Mundo!") # Cuerpo de la funcion
    print(f"Bienvenidoos jonnhy") # Cuerpo de la funcion

hola()# Llamada a la funcion

print("-----")

# Ejmplo con parametro.
def hola(nombre): # Definicion de la funcion
    print("Hola Mundo!")  # Cuerpo de la funcion
    print(f"Bienvenidoos {nombre}")

hola("Jonnhy")

print("-----")
# Ejmplo con varios parametro.
def hola(nombre, apellido): # Definicion de la funcion y sus parametros
    print("Hola Mundo!")
    print(f"Bienvenidoos {nombre} {apellido}") # Cuerpo de la funcion añadiendo varios parametros, antes definidos.

hola("Jonnhy", "Garcia") # Llamada a la funcion con varios argumentos, antes definidos como parametros.

print("-----")

# Emplo con valor por defecto.
def hola(nombre, apellido="De Leon"): # Definicion de la funcion y sus parametros, uno con valor por defecto con el signo ""="
    print("Hola Mundo!")
    print(f"Bienvenidoos {nombre} {apellido}") # Cuerpo de la funcion añadiendo varios parametros, antes definidos.

hola("Jonnhy") # Llamada a la funcion con un argumento, el otro toma el valor por defecto.

print("-----")

# Podemos elegir el ornde de los argumentos, usando argumentos con nombre cuando llamamos a una funcion.
# PERO SI PONENES UN VALOR A UN ARGUMENTO, TODOS DEBEN TENER VALOR ASIGNADO. no SE PUEDE MEZCLAR, uno con y otro sin.
hola(apellido="San Diego", nombre="Jonnhy") # Puedes elegir el orden dandoles un valor directo.

print("-----")

