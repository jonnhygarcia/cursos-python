# importar deque "dequiu", es una clase importada que gestiona la listas mas adecuadamente.
# Se le llama FIFO
from collections import deque

# las filas son como las colas de un cine, mediante se van atendiendo, se va, y el que siguie sube, hasta ser todos atendidos.
fila = deque([1, 2])
# fila.append(3)
# fila.append(4)
# fila.append(5)
print(fila)

fila.popleft()
fila.popleft()
print(fila)

if not fila:
    print("fila vacia")