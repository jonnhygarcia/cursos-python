# Almacenar OBJETOS dentro de OBJETOS y se le llaman Contenedores. 

# creamos una clase con las propiedades nombre y precio.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    # Creamos un string para mostar en pantalla con los productos y precios que agregaremos mas adelante.
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"

# Creamos una clase con la categoria, donde estara una lista vacia al principio para rellenar, con los productos agregados.
class Categoria:
    productos = []
    
    # Definimos el nombre y los productos
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    # Definimos un metodo para gregar productos a la lista vacia.
    def agregar(self, producto):
        self.productos.append(producto)
    
    # Definimos un metodo para imprimir los productos o mostrar en pantalla dichos productos.
    def imprimir(self):
        for producto in self.productos:
            print(producto)

# creamos los productos y las detalles de la clase Producto con su nombre y precio.
kayak = Producto("Kayak.", 1000)
bicicleta = Producto("Bicicleta.", 750)
surfboard = Producto("Surfboard.", 500)

# Creamos una categoria llamada deportes, donde metemos en la lista vacia unos productos de los creados antes.
deportes = Categoria("Deportes.", [kayak, bicicleta, "Producto: patines - Precio: 75"])

# Usamos la propiedad de Agregar, del la clase categoria, para agregar mas productos como es el caso del Surfboard.
deportes.agregar(surfboard)

# Usamos la propiedad de imprimir para mostrar la lista con todos los productos que en ella actualmente.
deportes.imprimir()
