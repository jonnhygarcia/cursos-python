#desempaquetado
lista1 = [1, 2, 3, 4]
print(lista1)

# operador de desempaquetamiento:
print(*lista1)

# Combiana varias listas mas agregamos strings.
lista2 = [5, 6]
combinada = ["hola", *lista1, "Mundo", *lista2]
print(combinada)

# De esta forma la ultima "y" sobrescribe la primera
punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

# Si se cambia el orden de "y" no la sobrescribe:
punto1 = {"y": 19, "n": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "hola mundo", **punto2}
print(nuevoPunto)
