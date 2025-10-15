# and, or, not controladores lógicos, precedencia y de corto circuito

gas = True
encendido = True
edad = 10

# El auto puede avanzar si tiene gas y está encendido y es mayor de 17 años
# if not gas and (encendido or edad > 17):
#     print("El auto puede avanzar")
# else:
# print("El auto no puede avanzar")

if not gas and encendido or edad > 17:
    print("El auto puede avanzar")
else:
    print("El auto no puede avanzar")