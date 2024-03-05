import random

# Solicitar al usuario el número de números aleatorios y el rango
cantidad_numeros = int(input("Ingrese la cantidad de números aleatorios a generar: "))
rango_inferior = int(input("Ingrese el límite inferior del rango: "))
rango_superior = int(input("Ingrese el límite superior del rango: "))

# Generar números aleatorios en el rango especificado
numeros_aleatorios = [random.randint(rango_inferior, rango_superior) for _ in range(cantidad_numeros)]

# Mostrar los números aleatorios generados
print("Números aleatorios generados:", numeros_aleatorios)
