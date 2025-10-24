# El constructor se ejecuta dentro de una clase, y este se va a ejecutar siempre que creemo una nueva instancia, como
# "__init__" por ejemplo, y se agrega self siempre "__init__(self))"
# self se usa para referenciar todas las nuevas instancias de las clases como "mi_perro".

class Perro:
    def __init__(self, nombre, edad): # Podemos pasar al constructor self(obligatorio), y mas valores "nombre", "edad".
        self.nombre = nombre # valores de propiedades para asignar en las proximas instancias abajo.
        self.edad = edad # valores de propiedades para asignar en las proximas instancias abajo.
    
    # En los metodos tambien podemos acceder a esas propiedades de los constructores con self.<nombre propiedad>
    def habla(self):
        print(f"{self.nombre} dice: Guau!")

# Agremos los argumentos "Chanchito" que hace referencia "nombre" y lo muestra.          
mi_perro = Perro("Chanchito", 1) # se ejecuta instancia, con las propiedades "nombre" y "edad"
mi_perro.habla() # al ejecutar la instancia, se ejecuta el metodo "habla" donde usamos la propiedad nombre con "self.nombre"

# Demostramos que self hace referencia a la isntancia de la clase, y no necesariamente es un valor compartido por todas las-
# instancias.
#mi_perro2 = Perro("Felipe")
print(mi_perro.nombre)
#print(mi_perro2.nombre)
