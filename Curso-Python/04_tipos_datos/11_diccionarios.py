# un diccionario cuenta de una llave, entre las llaves la parte derecha es un string y la otra puede ser cualquier cosa.
# En los diccionarios es importante que sea un string dos puntos (:) y luego el valor que sea, si son varios separados con comas.
punto = {"x": 25, "y": 50}
print(punto)

# No se solicita infirmacion a los diicionarios con indices sino se le llama al string en concreto a salicitar valor.
print(punto["x"])
print(punto["y"])

# Se puede agregar o crear mas elementos al diccionario de la siguiente manera:
punto["z"] = 45
print(punto)

# Si intentamos accder a un elemento que no existe dara error
# print(punto, punto["lala"])

# pero podemos consultar, preguntandole si existe y si no no respondera nada evitando el error.
if "lala" in punto:
    print("encontre lala", punto["lala"])

# acceder a un valor del diccionario con el metodo get para que no explote un error
# es importante poner una "key" 
print(punto.get("x"))
print(punto.get("lala")) # devuelve un none cuando no existe y no da error
print(punto.get("lala", 97)) # Incluso se puede asignar un valor por defecto en caso de que no exista ese valor

# Elimina el la llave con su valor incluido.
del punto["x"]
del (punto["y"]) 
print(punto)

punto["x"] = 25

# Te genera la llave y el valor
for valor in punto:
    print(valor, punto[valor])

# para crear unas tuplas con sus yaves y valor.    
for valor in punto.items():
    print(valor)

# Se puede desempaquetar tuplas para acceder a sus datos y valores.
for llave, valor in punto.items():
    print(llave, valor)

# Los diccionarios se usan para acceso a bases de datos, y de esta forma se muestra una forma de uso mas real
# En una base de datos de usuarios con sus ids, nombres, etc.. acceder con un for para encontrar los nombres de usuarios.
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]

# solicitamos nombres de usuarios.
for usuario in usuarios:
    print(usuario["nombre"])