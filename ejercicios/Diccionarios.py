# Los diccionarios en Python son estructuras de datos que almacenan pares clave-valor.
# Son mutables y desordenados, lo que significa que puedes cambiar su contenido pero no
# tienen un orden fijo. Se definen usando llaves {} y los pares clave-valor se separan por comas.
# Las claves deben ser únicas e inmutables (como cadenas, números o tuplas),
# mientras que los valores pueden ser de cualquier tipo de dato.        
# Crear un diccionario vacío
mi_diccionario = {}     
# Crear un diccionario con algunos pares clave-valor
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
# Acceder a valores usando claves
print(persona["nombre"])  # Salida: Juan
print(persona.get("edad"))  # Salida: 30
# Agregar o actualizar pares clave-valor
persona["profesion"] = "Ingeniero"  # Agrega una nueva clave-valor
persona["edad"] = 31  # Actualiza el valor de la clave "edad"
# Eliminar pares clave-valor        
del persona["ciudad"]  # Elimina la clave "ciudad"
# persona.pop("edad")  # Elimina y devuelve el valor asociado a la clave "edad"
# Longitud del diccionario
print(len(persona))  # Salida: 2 (después de eliminar "ciudad")
# Iterar sobre claves, valores o ambos
for clave in persona:
    print(clave, persona[clave])  # Imprime cada clave y su valor asociado
for clave, valor in persona.items():
    print(clave, valor)  # Imprime cada clave y su valor asociado
# Verificar si una clave existe en el diccionario
if "nombre" in persona:
    print("La clave 'nombre' existe en el diccionario")
# Métodos útiles de diccionarios
claves = persona.keys()  # Devuelve una vista de las claves
valores = persona.values()  # Devuelve una vista de los valores
pares = persona.items()  # Devuelve una vista de los pares clave-valor
# Limpiar el diccionario
persona.clear()  # Elimina todos los pares clave-valor
print(persona)  # Salida: {}        
# Ejemplo de diccionario anidado
estudiantes = {
    "123": {"nombre": "Ana", "edad": 20},   
    "456": {"nombre": "Luis", "edad": 22}
}
print(estudiantes["123"]["nombre"])  # Salida: Ana  
# conteo y agrupacion con diccionarios se usan para contar ocurrencias de elementos o clasificar datos.
frutas = ["manzana", "banana", "manzana", "naranja", "banana", "manzana"]
conteo_frutas = {}
for fruta in frutas:
    if fruta in conteo_frutas:
        conteo_frutas[fruta] += 1
    else:
        conteo_frutas[fruta] = 1
print(conteo_frutas)  # Salida: {'manzana': 3, 'banana': 2, 'naranja': 1}   
