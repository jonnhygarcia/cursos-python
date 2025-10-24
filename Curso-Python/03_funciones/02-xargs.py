# Ejemplo de uso de *args para recibir un número variable de argumentos posicionales en una función en Python.
# *args permite a una función aceptar cualquier cantidad de argumentos posicionales.    
# Los argumentos se reciben como una tupla dentro de la función.
# Esto es útil cuando no sabemos de antemano cuántos argumentos se pasarán a la función.
def suma(*numeros): # El asterisco (*) antes del parametro 'numeros' indica que puede recibir multiples argumentos posicionales.
    resultado = 0 # Inicializamos una variable para almacenar la suma.
    for numero in numeros: # Iteramos sobre cada numero en la tupla 'numeros', que contiene todos los argumentos pasados.
        resultado += numero # Sumamos cada numero al resultado de la suma.
    print(resultado) # Imprimimos el resultado de la suma de todos los numeros recibidos. IMPORTANTE LA IDENTACION, debe estar al nivel del for pero no dentro. 

suma(2, 5, 8) # Llamamos a la funcion 'suma' con tres argumentos posicionales y el resultado sera 15 ya que 2 + 5 + 8 = 15.
suma(2, 5) # Llamamos a la funcion 'suma' con dos argumentos posicionales y el resultado sera 7 ya que 2 + 5 = 7.
suma(2, 5, 7, 45, 32) # Llamamos a la funcion 'suma' con cinco argumentos posicionales y el resultado sera 91 ya que 2 + 5 + 7 + 45 + 32 = 91.

print("-----")