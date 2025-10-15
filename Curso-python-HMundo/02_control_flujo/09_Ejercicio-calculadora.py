# Calculadora por consola, indicar un numero e indicar que tiene que ingresar un numero y luego una operacion
# que ingrese otro numero y le devuelva el resultado de la operacion.
# RESUMEN: ingresa un nuevo la operacion que quieras que haga y el otro numomero y da el resultado de la operacion.

print(">> \" Bienvenido a la calculadora por consola \" ")
print(">> para salir ingresa 'salir' en cualquier momento")
print(">> Las operaciones ( suma, resta, multi, y div )")
print("---------------------------------------------------")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida")
        break

    print(f"El resultado es: {resultado}")
