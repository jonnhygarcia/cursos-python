""""estructuras de control if, elif, else"""

# if condiciona1:
    # bloque de instrucciones 1
# elif condiciona2:
    # bloque de instrucciones1 es falsa y concion2 es verdadera
# else:
    # bloque de instucciones3 si todas las anteriores son falsas para cerrar el codigo.
    
""""ejemplo de condicoinales"""
# pasa de una condicon a otra hasta que se cumpla, o al final ejecuta el else.
numero = 5

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")


# condicionales multiples elif
edad = 60
es_estudiante = True
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and es_estudiante:
    print("Eres un adulto y un estudiante")
else:
    print("Eres un adulto y no eres estudiante")
 
# Entrada de datos del usuario mezclado con condionales   
clima = input("?como esta el clima? (soleado, nublado, lluvioso): ")

if clima == "soleado":
    print("Hace buen dia para salir")
elif clima == "nublado":
    print("El clima esta nublado, lleva un sueter")
elif clima == "lluvioso":
    print("Lleva un paraguas, esta lloviendo")
else:
    print("No reconozco ese clima")
    

""" otro ejemplo complejob de condicionales"""

dia = input("introduce el dia de la semana: ").lower()

if dia == "lunes":
    print("Hoy es lunes, inicio de semana")
elif dia == "viernes":
    print("Hoy es viernes, es finde y el cuerpo lo sabe")
elif dia == "sabado" or dia == "domingo":
    print("Es fin de semana, a descansar")
else:
    print("Es un dia entre semana, a trabajar")