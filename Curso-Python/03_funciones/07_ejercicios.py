# Esta funcion elimina los espacios de una palabra o cadena de texto.
def no_space(texto):
    nuevo_texto = ""  # >> eliminta los espacios vacios
    for char in texto:  # >> recorre cada letra de la palabra o cadena de texto
        if char != " ":  # >> si la letra es distinto de un espacio vacio
            nuevo_texto += char  # >> añade la letra a la nueva palabra o cadena de texto
    # >> devuelve la palabra o cadena de texto sin espacios ninguno, toda la palabra seguida
    return nuevo_texto


# Esta funcion cambia el orden de una palabra o una cadena de texto.
def reverse(texto):
    texto_al_reves = ""  # >> crea un nuevo texto totalmente vacio
    for char in texto:  # >> recorre cada letra de la palabra o cadena de texto
        # >> va añadiendo las letras al reves, con += no funcionaria
        texto_al_reves = char + texto_al_reves
    return texto_al_reves  # >> devuelve la palabra o cadena de texto ya al reves al reves


# Utilizando las funciones anteriores, usamos en una funcion llamada es_palindromo que quita espacios y cambia el orden las palabras
# par acomprobar si son palimbros de alantre a tras y de atras a alante, aparte con lower() nos aseguramos que no hay problemas
# con las letras mayusculas y minusculas, convirtiendolas todas en micusculas y no de errores de entender las palabras.
def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower() # con este retorno podemos devolver un comparativo para que devuelva un bool en vez del texto, y saber si es palindromo devuelve verdadero sino devuelve falso. aparte lower() evita errores tipograficos al pasarlas todas a minusculas.


# La funcion reconoce esta oracion como palindromo por eso da True
print(es_palindromo("AmO la paloma"))
# La fucnion devuelve False ya que la Oracion no es palindromo
print(es_palindromo("Hola Mundo"))
print(es_palindromo("Anita lava la tina"))  # es palindromo por eso da True.
