usuarios = [
    ["Chanchito", 4], 
    ["Felipe", 1], 
    ["Pulga", 5]
]

# Esta seria la forma mas tradicional con for de sacar los nombres "indice 0" de una lista.   
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# Realiza una transformacion de  lista tambien llamada "map"
# nombres = [usuario[0] for usuario in usuarios] 
# print(nombres)

# filrtrar la lista. tambien llamada "filter"
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# Transformar y filtrar lista al mismo tiempo. le transformas seleccinando solo el idice que  quieres y filtras 
# aplicando un if con un orden, e indice.
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# La forma de usar map con funcion lambda.
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# La forma de usar filter con funcion lambda.
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)