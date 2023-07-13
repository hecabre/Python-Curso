#Primeros pasos
"""
edad = int(input("Cual es tu edad?"))

if edad == 18:
    print("Tienes 18")
    if edad == 19:
        print("Tienes 19")
else:
    print("No tienes 18")

"""
"""
for i in edades:
    print(f"Mi edad es {i}")


print("------------------------")
edades[0] = "Esta es la primera"
edades[1] = "Esta es la segunda"
edades[2] = "Esta es la tercera"

for i in edades:
    print(f"Este arreglo ha cambiado {i}")
"""

#nombres = [3, 2, 1]
#print(nombres)
#nombres.pop()
#print(nombres)
"""

numeros = []

for i in range(1, 11):
    numeros.append(i)
    
print(numeros)

for i in range(1, 11):
    numeros.pop()

print(numeros)
"""
"""
contador = 0

while True:
    contador += 1
    print(contador)
    if contador == 3:
        exit()

    if contador == 6:
        break


print("Hemos salido del ciclo")
"""
"""
edades = [i for i in range(1, 11)]

def mi_funcion(edad:int) -> str:
    Imprime el nombre y la edad de alguien

    Args:
        nombre (str): Nombre de una persona
        edad (int, optional): _Edad de una persona. Defaults to 50.
    
    
    print(edad)

for edad in edades:
    mi_funcion(edad)
"""

#lumno = {"nombre": "Juan", "edad": "30", "esp": 10}
alumno = ("Juan", 30)
print(alumno[0])
print(alumno[1])
