# Podemos concatenar strings, usando el operador + o las f-strings.
nombre = "Jonnhy"
apellido = "Garcia"
# aqui usamos el operador +, pero es mejor usar f-strings, porque es mas facil de leer y escribir, aparte se añade un espacio entre los nombres con las comillas.
nombre_completo = nombre + " " + apellido
# aqui usamos f-strings, que es la mejor forma de concatenar strings.
nombre_completos = f"{nombre} {apellido}"
print(nombre_completo)  # Jonnhy Garcia se mostraria en consola.
