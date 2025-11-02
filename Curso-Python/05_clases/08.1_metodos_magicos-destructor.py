class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Este seria el destructor de metodos magicos, para eliminar propiedades, y atraves de las instancias cuando se le llame
    # es un metodo magico que se ejecuta cuando eliminamso un metodo, al contrario de cuando se crea un motodo con el 
    # contructor que se crea a raiz de crear el metodo.
    def __del__(self):
        print(f"Chao perro 😒 {self.nombre}")
    
    def __str__(self):
        return f"Clase Perro: {self.nombre}"
    
    def habla(self):
        print(f"{self.nombre} dice: Guau!")

perro = Perro("Chanchito", 7)
del perro