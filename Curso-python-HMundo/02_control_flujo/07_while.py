# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

# se le da a la variable comando un valor vacio.
comando = ""
# se inicia un bucle while que continuará hasta que el valor de comando sea "salir" (sin importar mayúsculas o minúsculas).
while comando.lower() != "salir": # -> se usa lower() para convertir cualquier texto que se introduzca en minusculas.
    comando = input("Ingrese un comando (escriba 'salir' para terminar): ")
    print(f"Comando ingresado: {comando}") # -> se imprime el string comando ingresado por el usuario.

# es importante que cuando se pide datos al uusuiario, este puede escribirlo mal por error, y con el lower() se evita el error.

# para controlar un loop infinito no es mala practica por un brake donde creemos que puede darse dicho loop infinito.
