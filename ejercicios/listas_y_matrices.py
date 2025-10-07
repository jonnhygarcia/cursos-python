# Las liastas son colecciones ordenadas y mutables que permiten almacenar múltiples elementos en una sola variable.
mi_lista = []

# Crear una lista con algunos elementos
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Luis", "Carlos"]
mixtas = [1, "Hola", 3.14, True]

# Agregar elementos a una lista usando append()
mi_lista = [1, 2, 3]
mi_lista.append(4)  # mi_lista ahora es [1, 2, 3, 4]
mi_lista.insert(1, 10)  # mi_lista ahora es [1, 10, 2, 3, 4]

# Eliminar elementos de una lista usando remove() o pop()
mi_lista.remove(10) # mi_lista ahora es [1, 2, 3, 4] otra vez
mi_lista.pop()  # Elimina el último elemento, mi_lista ahora es [1, 2, 3]

# Longitud de una lista
print(len(mi_lista))  # Salida: 3

contador = 0 while contador < 3: print(contador) contador += 1 