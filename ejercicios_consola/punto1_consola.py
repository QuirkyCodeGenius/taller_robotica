# Pedir al usuario que ingrese el valor de corriente y voltaje
corriente = float(input("Ingrese el valor de corriente (en amperios): "))
voltaje = float(input("Ingrese el valor de voltaje (en voltios): "))

# Calcular la potencia usando la fórmula P = I * V
potencia = corriente * voltaje

# Mostrar el resultado
print("La potencia consumida por el circuito es:", potencia, "vatios")
