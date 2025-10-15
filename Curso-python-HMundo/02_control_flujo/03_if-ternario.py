"""
# if ternario
# es una forma compacta de escribir un if 
# se usa para asignar un valor a una variable en funcion de una condicion
# se escribe en una sola linea
# se usa la sintaxis: valor_si_verdadero if condicion else valor_si_falso"""

edad = 19

# es un ejemplo de if ternario, que es una forma mas compacta de escribir un if else
mensaje = "Es mayor" if edad >= 17 else "Es menor"

''' 
es un ejemplo de if else normal
# if edad >= 17:
#     mensaje = "Es mayor"
# else:
#     mensaje = "Es menor" 
'''

print(mensaje)