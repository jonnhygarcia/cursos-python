# Metodos de strings, formatos y f-strings posibles y ejemplos utiles.
animal = "  chanCHito feliz  "  # string con espacios y mayusculas y minusculas
print(animal.upper())  # convierte todo a mayusculas
print(animal.lower())  # convierte todo a minusculas

# convierte la primera letra en mayuscula y las demas en minuscula
print(animal.strip().capitalize())
print(animal.title())  # convierte la primera letra de cada palabra en mayuscula
print(animal.strip())  # elimina espacios a la derecha e izquierda
print(animal.rstrip())  # elimina espacios a la derecha
print(animal.lstrip())  # elimina espacios a la izquierda
print(animal.count("cito"))  # cuenta cuantas veces aparece la subcadena

# devuelve True si la cadena empieza con la subcadena
print(animal.startswith("chan"))

# devuelve el indice de la primera aparicion de la subcadena en este cas "ch" al no existir devuelve -1
print(animal.find("cH"))

# reemplaza la subcadena por otra subcadena y devuelve una nueva cadena, cambiando chanCHito por perrito
print(animal.replace("chanCHito", "perrito"))

# busca la subcadena desde el final de la cadena
print(animal.rfind("cH"))
print("ch" not in animal)  # devuelve True si la subcadena no esta en la cadena

# poner al reves el string
print(animal[::-1])  # invierte el string
