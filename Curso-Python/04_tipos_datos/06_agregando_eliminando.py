mascotas = ["Pelusa", 
            "jonnhy", 
            "Pulga", 
            "Felipe", 
            "jonnhy", 
            "Chanchito feliz"]

# Insertar un elemento en la pocision que queramos.
mascotas.insert(1, "Melvin")

# Te agrega al final de la lista un elemento.
mascotas.append("Chanchito triste")

# Elimita el elemento indicado
mascotas.remove("Pulga")

# Elimina el ultimo elemento, pero si le dices un idece, te borra el que iniques.
mascotas.pop(1)

# Elimina el idice que le digas con "del"
del mascotas[0]

#con clear elimitas toda la lista al completo.
mascotas.clear()

print(mascotas)