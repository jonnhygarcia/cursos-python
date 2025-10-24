# Ejemplo de return para devolver un valor desde una función en Python.
# La instrucción return permite a una función devolver un valor al lugar donde fue llamada.
# Esto es útil cuando queremos que una función realice un cálculo y nos devuelva el resultado
# para usarlo posteriormente en nuestro código. 

# Sin return: la función imprime el resultado pero no lo devuelve.
def suma(a, b):
    resultado = a + b
    print(resultado)

suma(3, 5)

print("-----")

# Con return: la función devuelve el resultado para usarlo posteriormente.
def suma(a, b):
    resultado = a + b
    return resultado
# Llamamos a la función y almacenamos el valor devuelto en una variable.
c = suma(1, 2) # La variable c ahora contiene el valor devuelto por la función 1+2=3. 
# Podemos usar el valor devuelto en otras operaciones.
d = suma(c, 2) # La variable d ahora contiene el valor 3+2=5.ya que c=3, como resultado de la llamada anterior.
print(d) # Imprimimos en pantalla el valor de d, que es 5.
# De esta forma, el uso de return nos permite reutilizar los resultados de las funciones en nuestro código.

print("-----")
