import math

# Preguntar al usuario qué tipo de sólido desea calcular
opcion = int(input('Seleccione el tipo de sólido (1=Prisma, 2=Pirámide, 3=Cono truncado, 4=Cilindro): '))

# Según la opción seleccionada, solicitar los parámetros necesarios y calcular el volumen correspondiente
if opcion == 1:  # Prisma
    # Pedir al usuario la base y la altura del prisma
    base = float(input('Ingrese el área de la base del prisma: '))
    altura = float(input('Ingrese la altura del prisma: '))
    
    # Calcular el volumen del prisma
    volumen = base * altura

elif opcion == 2:  # Pirámide
    # Pedir al usuario la base y la altura de la pirámide
    base = float(input('Ingrese el área de la base de la pirámide: '))
    altura = float(input('Ingrese la altura de la pirámide: '))
    
    # Calcular el volumen de la pirámide
    volumen = (1/3) * base * altura

elif opcion == 3:  # Cono truncado
    # Pedir al usuario el radio de las bases y la altura del cono truncado
    radio_superior = float(input('Ingrese el radio superior del cono truncado: '))
    radio_inferior = float(input('Ingrese el radio inferior del cono truncado: '))
    altura = float(input('Ingrese la altura del cono truncado: '))
    
    # Calcular el volumen del cono truncado
    volumen = (1/3) * math.pi * altura * (radio_superior**2 + radio_inferior**2 + radio_superior * radio_inferior)

elif opcion == 4:  # Cilindro
    # Pedir al usuario el radio y la altura del cilindro
    radio = float(input('Ingrese el radio del cilindro: '))
    altura = float(input('Ingrese la altura del cilindro: '))
    
    # Calcular el volumen del cilindro
    volumen = math.pi * radio**2 * altura

else:
    # Si se selecciona una opción inválida, mostrar un mensaje de error
    print('Opción inválida. Saliendo del programa.')
    exit()

# Mostrar el volumen del sólido calculado
print('El volumen del sólido es:', volumen)
2