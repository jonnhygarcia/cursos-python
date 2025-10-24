# En las clases tanto propiedades como atributos es exactamente lo mismo, hay unas propiedades exclusivamente llamadas 
# propiedades que se explicaran mas adelante.

class Perro:
    patas = 4 # creo una propiedad de clase, y todas las instanacias que se creen, tendrán esta propiedad si la pieden.
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.edad = edad 
    
    def habla(self):
        print(f"{self.nombre} dice: Guau!")

# Ahora en vez de 5 que se deficion en la clase, seran 3 al modificarse.
Perro.patas = 3 # desde la instancia se puede modificar la propiedad para darle otro valor.
mi_perro = Perro("Chanchito", 1) 

mi_perro.patas = 5 # aqui modificamos la propiedad pero solo para 
mi_perro2 = Perro("Felipe", 1)
print(Perro.patas)

# ahora la instancia mi perro tendran 5 porque se modifico la instancia, no la clase, con lo que las
# posteriores seguiran teniendo 3 ya que fue la ultima modificacion de la propiedad.
print(mi_perro.patas) 

# Aqui al no tener modificacion de instancias, toma el valor de la ultima modificacion de la clase que es "3"
print(mi_perro2.patas)

# -> podemos crear una propiedad para una clase, y toda las instancias que llamen a esa clase tendran la misma propiedad
# -> podemos modificar este valor en una instancia concreta si queremos que vez de 5 sea 3
# -> Los ultimos valores de las propiedades de clase seran los que se apliquen a las demas instancias que se creen.