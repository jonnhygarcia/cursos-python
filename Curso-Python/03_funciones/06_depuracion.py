# Para deporar este codigo hacemos un codigo con el error, que no lee todos los caracteres, solo devuelve 1
# def largo(texto):
#     resultado = 0
#     for _ in texto:
#         resultado += 1
#         return resultado

# l = largo("Hola Mundo")
# print(l)

# Codigo en depuracion, que ya lee todos los caracteres y devuelve el largo correcto
def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("Depurando codigo...")
l = largo("Hola Mundo")
print(l)
