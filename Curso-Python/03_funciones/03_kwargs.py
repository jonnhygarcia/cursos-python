# Ejemplo de kwargs para recibir un número variable de argumentos con nombre en una función en Python.
# **kwargs permite a una función aceptar cualquier cantidad de argumentos con nombre (clave-valor).    
# Los argumentos se reciben como un diccionario dentro de la función.
# Esto es útil cuando no sabemos de antemano cuántos argumentos con nombre se pasarán a la función.
def get_product(**datos): # El parámetro **datos captura todos los argumentos con nombre en un diccionario.
    print(datos["id"], datos["name"], datos["desc"]) # Accedemos a los valores del diccionario usando sus claves, para aplicar los nombres y su futuro valor.

get_product(id=1, name="iPhone", desc="Un tipo de telfono") # Llamamos a la función pasando argumentos con nombre y su valor.
# De esta form podemos agregar parametros y argumentos en la misma llamada de la funcion.