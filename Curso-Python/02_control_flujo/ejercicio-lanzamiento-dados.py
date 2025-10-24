import random

num_lanzamientos = int(input("¿Cuántas veces quieres lanzar el dado? "))
if num_lanzamientos <= 0: 
    print("El número de lanzamientos debe ser mayor a 0.")    
    exit()
resultados = [0] * 6

for _ in range(num_lanzamientos):    
    cara = random.randint(1, 6)    
    resultados[cara - 1] += 1
if num_lanzamientos == 1: 
    print(f"Salió la cara: {cara}")
else: 
    for i in range(6):        
        porcentaje = (resultados[i] / num_lanzamientos) * 100 
        print(f"Porcentaje de veces que salió la cara {i+1}: {porcentaje:.2f}%")