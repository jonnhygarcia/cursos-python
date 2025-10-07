# argumentos basicos Posicionales y formas de funciones
def dividir(a, b):
    """
    Divide dos numeros y devuelve el resultado.
    """
    if b == 0:
        return "Error: No se puede dividir por cero." # Se muestra este error si se intenta divivir por cero.
    return a / b  # si es otro numero devuelve el restultado de la division.

resultado = dividir (10, 2)
print(f"El resultado de la division es: {resultado}")

# Argumentos Nombrados o palabras clave.
def formatear_fecha(dia, mes, anio):
    """
    Formatea una fecha en el formato DD/MM/AAAA.
    Args:
        dia (_type_): _description_
        mes (_type_): _description_
        anio (_type_): _description_
    """
    return f"{dia:02d}/{mes:02d}/{anio}"

fecha = formatear_fecha(mes=12, dia=25, anio=2025)
print(fecha)

# Argumentos por defecto
def generar_informe(nombre, estado="pendiente"):
    """"
    Genera un informe del estado de la tarea para un usuario.
    Args:
        nombre (_type_): _description_
        mensaje (str, optional): _description_. Defaults to "pendiente".
    """
    return f"informe: {nombre}, estado de la tarea: {estado}"
print(generar_informe("proyecto A")) # usa el valor por defecto "pendiente"

print(generar_informe("proyecto B", estado="completo")) # usa el valor proporcionado "completo"

# Argumentos variables "*arg"  y "**kwargs"
def sumar_todo(*numeros):
    """
    Suma una cantidad variable de numeros y devuelve el resultado.
    """
    return sum(numeros)
    print(sumar_todo(1, 2, 3, 4)) # devuelve 10
 
# **kwargs recoge argumentos nombrados adicionales en un diccionario.
def mostrar_informacion(**datos): 
     for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_informacion(nombre="Luis", edad=30, ciudad="Madrid")

# Ejercicio de combinacion de todos los tipos de argumentos
def crear_pedido(producto, cantidad=1, *extras, **detalles):
    """
    Crea un pedido con informacion del cliente, producto, cantidad, extras y detalles adicionales.
    """
    print(f"Producto: {producto}")
    print(f"Cantidad: {cantidad}")
    if extras:
        print(f"Extras: {', '.join(extras)}·")
    for clave, valor in detalles.items():
        print(f"{clave}: {valor}")
        
crear_pedido("Pizza", 2, "extra queso", "sin gluten", cliente="carlos", entrega="domicilio")
        
        