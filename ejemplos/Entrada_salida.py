import csv
with open("datos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "Edad"])
    escritor.writerow(["Ana", 45])
    
    with open("datos.csv", "r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)
