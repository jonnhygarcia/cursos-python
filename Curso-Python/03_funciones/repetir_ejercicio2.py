#definir  funcion para elimitar espacios
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

texto = "hola que hace tio"
resultado = no_space(texto)
print(resultado)

def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves

texto = "contratar"
resultado = reverse(texto)
print(resultado)

