# Metodos 
class Perro:
    patas = 4 # creo una propiedad de clase, y todas las instanacias que se creen, tendrán esta propiedad si la pieden.
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.edad = edad 
    
    @classmethod
    def habla(cls):
        print(f"Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 4)
        
Perro.habla()
Perro1 = Perro("Chanchito", 2)
perro2 = Perro("Felipe", 2)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)