# set significa grupo o conjunto

# Set te limpia las lista eliminando los duplicados automaticamente.
# primer = {1, 1, 2, 2, 3, 4}
# print(primer)

# puedes agregar con "add( elemento)"
# primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5] # una lista no es un Set
segundo = set(segundo) #reemplaza la lista en un set, en base a una lista o tupla.
print(segundo)

# operadores de set en python

#Union:
print(primer | segundo) # Une varios sets y aplica el eliminar los duplicados y te da la lista combinada y limpia.

# interseccion: 
print(primer & segundo) # Busca las coincidencias de ambos sets y solo muestra los numeros que coinciden en ambos.

# difrencia: 
print(primer - segundo) # calcula la diferencias de los dos sets, quitando las coincidencias del primer set.

# diferencia simetrica
print(primer ^ segundo) # Los duplicados que coincidan de cada sets los elimina solo dejando los diferentes de cada set.

# el problema de los sets es que no se encuentran ordenados y no se puede acceder de forma directas a los mismos
#segundo[0] # da error

# Puedes accerder a ellos indirectamente, con for, y otras operaciones pero no direactas, por ejemplo puedes
# solicitar que si un numero se encutra en un set que devuelva algo en este caso "hola mundo"
if 5 in segundo:
    print("hola mundo")