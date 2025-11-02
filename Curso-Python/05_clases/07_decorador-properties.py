class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    #Creamos de forma privada la propiedad que queremos obtener y queremos modificar, evitando los Getter, y Setter, y 
    # demasiado codigo inhnecesario. Sin necesidad de contaminar con mas metodos de la cuenta, las instancias de nuestras 
    # clases.
    @property
    def nombre(self):
        print("pasando por Getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por Setter")
        if nombre.strip():
            self.__nombre = nombre

perro = Perro("choclo")
print(perro.nombre)