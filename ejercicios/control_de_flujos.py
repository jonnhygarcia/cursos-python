while True:
    print("Menu:")
    print("1. Saludar")
    print("2. Mostras numeros")
    print("3. Salir")
    
    opcion = input("Elige una opcion (1-3): ")
    
    if opcion == "1":
        print("---------------------------------------")
        print(">> Hola! Bienvenido al programa.")
        print("---------------------------------------")
    elif opcion == "2":
        for i in range(2, 6):
            print("---------------------------------------")
            print(f">> Número: {i}")
            print("---------------------------------------")
    elif opcion == "3":
        print("---------------------------------------")
        print(">> Saliendo del programa. ¡Adiós!")
        print("---------------------------------------")
        break
    else:
        print("---------------------------------------")
        print(">> Opción no válida. Por favor, elige una opción del 1 al 3.")
        print("---------------------------------------")
    