# inicio
# definir clientes y compras:
# crear variable str "cliente1" = valores (int) 200
# crear variable str "cleint2" =  valores (int) 100
# crear variable str "cliente3" = valores (int) 150

# creamos funcion:
# si total cliente es mayor o igual a 150€

# crear diccionario con datos de cliente, monto, y demas
# claveles(str) + valor(int) 

# Una lista con los IDs de los clientes que califican para la promocion.
# fin

def aplicar_promocion(compras):
    clientes_con_promocion = []
    for cliente, monto in compras.items():
        if monto >= 150:
            clientes_con_promocion.append(cliente)
    return clientes_con_promocion

compras = {    
    'Cliente1': 200,    
    'Cliente2': 100,
    'Cliente3': 180
}

clientes_promocion = aplicar_promocion(compras)
print(clientes_promocion)

# resultado: ['Cliente1', 'Cliente3']