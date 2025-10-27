# propiedades privadas.
class Perro:
    def __init__(self, nombre, edad): 
        self.__nombre = nombre  # se crea propiedad privada con poner dos giones bajos delante del nombre
        self.edad = edad 

    def habla(self):
        print(f"{self.__nombre} dice: Guau!") # luego de defirla, las puedes usar en el codigo, y seran siempre privadas.

    def get_nombre(self):
        return self.__nombre # forma de crar un metodo que nos devuelva el nombre privado get_nombre
    
    # Tambien se puede crear metodos privados con dos guiones bajos al comienzo del metodo ejemp: "__get_nombre"
    def set_nombre(self, nombre):
        self.__nombre = nombre # podemos cambiar el nombre privado con este metodo set_nombre
        

    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 4)

perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre()) # para obtener el nombre privado de perro, que antes no se podia, a atraves de una nueva variable.
print(perro1.__dict__) # se muestra diccionario de las clases privadas y sus restultado.
print(perro1._Perro__nombre) # forma de saltarse la privacidad de __noombre al crear un diccionario y nos devuelva la clase privada la renombranos en un print y nos muestra la clase privada, es una mala praxis, pero para urgencias puede ser util.

