# Podamos usar las """ para cometario mas largos y usarlo en una variable y llamarla en una funcion como print.
nombre_curso = "ultimate python"
descripcion_curso = """ 
Este curso esta diseñado para aprender python desde cero
y llegar a un nivel avanzado.
"""
print(nombre_curso, descripcion_curso)

# Con len podemos saber la cantidad de caracteres que tiene un string
print("cantidad de caracteres de un string:")
print(len(nombre_curso))
print("")

# Podemos usar los indices para acceder a los caracteres de un string
print("acceder a los caracteres de un string:")
print(nombre_curso[0])  # u muestra el primer caracter del string
print(nombre_curso[1])  # l muestra el segundo caracter del string
print(nombre_curso[-1])  # n muestra el ultimo caracter del string
print(nombre_curso[-2])  # o muestra el penultimo caracter del string
print(nombre_curso[0:8])  # ultimate muestra desde el indice 0 hasta el 7
print(nombre_curso[9:])  # python muestra desde el indice 9 hasta el final
print(nombre_curso[:8])  # utlimate muestra los primeros 8 caracteres
print(nombre_curso[:])  # utlimate python atrega todo el string al completo
print("")
# Podemos usar los metodos de los strings
print("metodos de los strings:")
print(nombre_curso.upper())  # ULTIMATE PYTHON
print(nombre_curso.lower())  # utlimate python
print(nombre_curso.title())  # Utlimate Python
print(nombre_curso.capitalize())  # Utlimate python
print(nombre_curso.replace("python", "JavaScript"))  # utlimate JavaScript
print(nombre_curso.find("python"))  # 9
print(nombre_curso.split(" "))  # ['ultimate', 'python']
print("")
# Podemos usar los metodos de los strings para eliminar espacios en blanco
print("eliminar espacios en blanco:")
nombre_curso_espacios = "   ultimate python   "
print(nombre_curso_espacios.strip())  # ultimate python
print(nombre_curso_espacios.lstrip())  # ultimate python
print(nombre_curso_espacios.rstrip())  # ultimate python
print("")
# Podemos usar los metodos de los strings para verificar si un string contiene otro string
print("verificar si un string contiene otro string:")
print("python" in nombre_curso)  # True
print("java" in nombre_curso)  # False
print("")  # Podemos usar los metodos de los strings para verificar si un string empieza o termina con otro string
print("verificar si un string empieza o termina con otro string:")
print(nombre_curso.startswith("ultimate"))  # True
print(nombre_curso.endswith("python"))  # True
print(nombre_curso.endswith("java"))  # False
print("")
# Podemos usar los metodos de los strings para contar la cantidad de veces que aparece un string
print("contar la cantidad de veces que aparece un string:")
print(nombre_curso.count("python"))  # 1
print(nombre_curso.count("java"))  # 0
print("")  # Podemos usar los metodos de los strings para verificar si un string es un numero
print("verificar si un string es un numero:")
numero = "123"
print(numero.isdigit())  # True
print(nombre_curso.isdigit())  # False
print("")  # Podemos usar los metodos de los strings para verificar si un string es alfabetico
print("verificar si un string es alfabetico:")
print(nombre_curso.isalpha())  # False
print("ultimate".isalpha())  # True
print("")  # Podemos usar los metodos de los strings para verificar si un string es alfanumerico
print("verificar si un string es alfanumerico:")
print(nombre_curso.isalnum())  # Falses
print("ultimatepython".isalnum())  # True
