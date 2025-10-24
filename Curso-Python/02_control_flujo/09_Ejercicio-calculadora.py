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
    try: # -> se intenta convertir n2 a entero, si falla se convierte a float.
        n2 = int(n2) # -> se intenta convertir n2 a entero.
    except ValueError: # -> si falla la conversion a entero, y da error de valores incorrectos...
        n2 = float(n2) # -> se convierte a float. En decimales por si quieres restar 0.xxx a un nuemero.

    if op.lower() == "suma": # -> se usa lower() para que no importe si se escribe en mayusculas o minusculas y si es igual a suma.
        resultado += n2  # -> se suma el resultado con n2 y se guarda en resultado.
    elif op.lower() == "resta": 
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida") # -> si no es ninguna de las operaciones validas se indica que no es valida.
        break

    print(f"El resultado es: {resultado}") # -> se imprime el resultado de la operacion, que se haya elegido.
