# print(1 > 2)
# print(1 < 2)
# print(1 >= 2)
# print(1 <= 2)
# print(2 >= 2)
# print(2 <= 2)
# print(1 == 2)
# print(1 != 2)
# print(1 != 1)

# print("")

# Pido que se introduzca un numero, pero importante convertirlo en entero con "int()" para que lo reconozca como tal, no como un string, suele ser un error comun.
# numero = int(input("intresa un numero menor que 2: "))
# if (numero < 2):
#     print("verdadero")
# else:
#     print("falso")

# print("")

# numero = int(input("Ingresa una contraseña: "))
# if numero == 1234:
#     print("Contraseña Corracta!")
# else:
#     print("Contraseña incorrecta!")

intentos = 0
pass_correcta = 1234

while True:
    numero = int(input("Ingresa una contraseña: "))

    if numero == pass_correcta:
        print("Contraseña Correcta!")
        break
    else:
        intentos += 1
        print("Contraseña incorrecta!")

        if intentos >= 3:
            print("Has superado el numero de intentos maximos.")
            break
