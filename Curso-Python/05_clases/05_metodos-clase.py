# Metodos 
class Perro:
    patas = 4 # creo una propiedad de clase, y todas las instanacias que se creen, tendrán esta propiedad si la pieden.
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.edad = edad 
    
    @classmethod
    def habla(cls):
        print(f"Guau!")
        
Perro.habla()
Perro1 = Perro("Chanchito", 2)
perro2 = Perro("Felipe", 2)