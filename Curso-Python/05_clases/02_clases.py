class Perro:
    def habla(self):
        print("Guau!")

mi_perro = Perro()
print(type(mi_perro))
print("-----")
print(" ")
mi_perro.habla()
print(isinstance(mi_perro, Perro)) # Preguntamos si "mi_perro" es una instancia de mi Clase "Perro" devuelve True
print(isinstance(mi_perro, str)) # Si pregunto si "mi_perro" es instancia de la Clase "str" inexistente aun seria False