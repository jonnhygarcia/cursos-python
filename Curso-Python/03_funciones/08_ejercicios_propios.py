print(" ")
print("----")
print(" ")
# Definimos una fucion para quitar espacios a una frase o string.
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

# Probamos que la funcion "no_space()"" funnciona, quita los espacios en una frase, recorriendo los caracteres.
texto =  "canto de mañana por la mañana" # le decimos una frase de prueba
resultado = no_space(texto) # le decismos que el resultado es la ejecucion de la funcion no_space() con el texto anterior.
print("Resultado funcion \"no_space()\" :")
print(">>", resultado) # Imprimimos en pantalla el resultado de "resultado" para ver que devuelve en este caso la frase al reves.

print(" ")
print("----")
print(" ")

# Definimos funcion para dar la vuelta a una frase.
def reverse(texto): # definimos la funcion reverse con el parametro texto.
    texto_al_reves = "" # Se crear una variable vacia.
    for char in texto: # Se recorre tacada caracter del parametro texto.
        texto_al_reves = char + texto_al_reves # A la variable vacia texto_al_reves, se le va atregando las char del parametro texto de lante de derecha a izquierda una delante de otra con lo que da la sensacion de ponerlas al reves.
    return texto_al_reves # devuelve el resutado de la funcion.

# Probamos que la funcion anterior "reverse()" funciona bien, con este pequeño codigo.
texto = "contigo"
resultado = reverse(texto)
print("Resultado funcion \"reverse()\" :")
print(">>", resultado)

print(" ")
print("----")
print(" ")

#Funcion para saber si una palabra es palindromo, o frase con es_palindromo
def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()

# Primer "resultado" de "texto" es palindromo con lo que dara True.
texto = "Anita lava la tina"
# Segundo "resultado2" de "texto2" no es palindromo con lo que dara False
texto2 = "Hola Mundo"
resultado = es_palindromo(texto)
resultado2 = es_palindromo(texto2)
print("Resultado funcion \"es_palindromo()\" :")
print(">>", resultado)
print(">>", resultado2)

print(" ")
print("----")
print(" ")