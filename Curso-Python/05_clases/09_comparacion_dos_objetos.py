class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # comnpara si son iguales aunque esten en diferentes espacios de memoria.
    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon
    
    # compara si son distintos el uno del otro.
    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon
    
    # mayor o igual
    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon
    
    # menor o igual
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon
       
coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

# Averigua si con el mismo en el mismo espacio de memoria, y no lo estan.
# print(coords == coords2)

# Averiguamos en que espacios de memoria estan y vemos mas informacion de la instancia.
# print(coords, coords2)

# Ahora al agregar el metoddo magico __eq__ podemos comparar auque no esten en el mismo espacio de memoria
# print(coords == coords2)

# Tambien pòpdemos comprobar la no igualdad con __ne__ non equal
# print(coords != coords2)

# Averiguar si es mayor o menor el uno del otro.
# print(coords < coords2)

# Averiguar si es menor o igual que el uno del otro.
print(coords <= coords2)