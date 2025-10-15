class Estudiante:
    def __init__(self, nombre, edad):
        self.Nombre = nombre
        self.Edad = edad
        self.Asignaturas = []

    def matricular(self, asig):
        self.Asignaturas.append(asig)

    def mostrar(self):
        print("Alumno:")
        print("-------")
        print(self.Nombre)
        print(f"{self.Edad} Años")
        print("Asignaturas:")
        print("-------")
        for i in range(len(self.Asignaturas)):
            print(f"Asignatura {i+1}: {self.Asignaturas[i]}")


# Crear objeto y usar métodos
nuevo = Estudiante("Jesús Martín", 45)
nuevo.matricular("Programación")
nuevo.matricular("Estadística")
nuevo.mostrar()
