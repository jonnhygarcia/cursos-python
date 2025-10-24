mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]

# for mascota in mascotas:
#     print(mascotas)

# Al igual de poder selecionar indice, y valor como en las lista vistas antes...
primero, segundo, = [1, 2]

# Tambien en un for, podemos usar el indice, lo que viene siendo una Tupla, que mas adelante se detallara.
# Lo que hace es que se declara un indice, y la lista de mascotas, y con enumerate nos las enumera en forma de lista
# Ahora se puede indicar el indice y el valor con print(indice, mascota)
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)