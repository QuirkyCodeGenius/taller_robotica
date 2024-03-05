import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Pedir al usuario que ingrese los valores
K = float(input('Ingrese la constante de ganancia (K): '))
wn = float(input('Ingrese la frecuencia natural no amortiguada (wn): '))
cita = float(input('Ingrese el coeficiente de amortiguamiento (cita): '))

# Crear la función de transferencia
numerator = [K * wn**2]
denominator = [1, 2 * cita * wn, wn**2]
sys = ctrl.TransferFunction(numerator, denominator)

# Determinar el tipo de sistema
if cita < 1:
    if cita > 0:
        system_type = 'Subamortiguado'
    else:
        system_type = 'Sin amortiguamiento'
elif cita == 1:
    system_type = 'Críticamente amortiguado'
else:
    system_type = 'Sobreamortiguado'

print('Tipo de sistema:', system_type)

# Graficar la respuesta al escalón
time, response = ctrl.step_response(sys)
plt.plot(time, response)
plt.title('Respuesta al escalón')
plt.grid(True)
plt.show()
