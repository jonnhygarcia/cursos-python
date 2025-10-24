from datetime import datetime

productos = [
    {'nombre': 'Manzana', 'precio': 0.5},
    {'nombre': 'Pera', 'precio': 0.70},
    {'nombre': 'Pan', 'precio': 1.0},
    {'nombre': 'Leche', 'precio':  4.50},
    {'nombre': 'Manzana', 'precio': 0.5},
    {'nombre': 'Pan', 'precio': 1.0},
]

def generar_ticket(productos):
    contador_productos = {}
    fecha = datetime.now().strftime("%d/%m/%Y")
    for p in productos:
        nombre = p['nombre']
        precio = p['precio']
        if nombre in contador_productos:
            contador_productos[nombre]['cantidad'] += 1
        else:
            contador_productos[nombre] = {'precio': precio, 'cantidad': 1}

    print("-------------------")
    print("Ticket de compra:")
    print("-------------------")
    print(f"Fecha: {fecha}")
    print("-------------------")
    total = 0
    for nombre, info in contador_productos.items():
        precio = info['precio']
        cantidad = info['cantidad']
        subtotal = precio * cantidad
        total += subtotal
        print(f"{nombre} x {cantidad} = {subtotal:.2f}€")       
    print("--------------------")
    print("Cantidad total: ", cantidad)
    print(f"Total: {total:.2f}€")
    print("--------------------")

    return total

generar_ticket(productos)

"""
tiene que ver con los punteros de C?
"""