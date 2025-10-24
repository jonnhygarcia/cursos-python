# Formato de cadenas, darle valor a una variable y usarla en un string.
nombre = "Juan"  # Asignacion de variable un string o cadena de texto.

# Asignacion de variable un entero int o numero entero.
edad = 30

# Usando f-string (formato literal de cadena) para insertar variables en un string. Las variables creadas antes se introducen dentro de llaves {} en el string, precedido por la letra f.
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# Usando el metodo format
print("Hola, mi nombre es {} y tengo {} años.".format(nombre, edad))
