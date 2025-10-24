# Se crear una clase con declarandola con "class", debe estar en PascalCase o UpperCamelCase con la primera letra mayusculas.
# Si escribimos mi perro seria "MiPerro".
class Perro:
    def habla(self): # se define la funcion que se llamaran a partir de ahora "Metodos", y se incluyen "self" siempre.
        print("Guau!")

# Creamos una instanacia de la clase de perro, a una variable se le agrega la clase "Perro()" sabesmos que es clase al ser PascalCase o UpperCamelCase.
mi_perro = Perro()
print(type(mi_perro)) # Imprimirmos para que indique que es una clase perro, con su modulo, y nombre de clase.
print("-----")
print(" ")

# no necesitaria agregar ningun argumentos, se lo pasa python con "self".
mi_perro.habla() # al crear la clase y un punto, ya aparecen las clases creadas, en este caso "habla" con un cubo morado

# isinstances recibe dos argumento, la instancia y la clase, y las compara, para sabes si son True o False.
print(isinstance(mi_perro, Perro)) # Preguntamos si "mi_perro" es una instancia de mi Clase "Perro" devuelve True
print(isinstance(mi_perro, str)) # Si pregunto si "mi_perro" es instancia de la Clase "str" inexistente aun seria False