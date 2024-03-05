import numpy as np
import matplotlib.pyplot as plt

def pt100_resistencia(temperatura):
    # Ecuación de conversión de temperatura a resistencia para PT100
    # Puedes ajustar los coeficientes según la especificación de tu sensor PT100
    A = 3.9083e-3
    B = -5.775e-7
    R0 = 100.0  # Resistencia a 0°C

    resistencia = R0 * (1 + A * temperatura + B * temperatura**2)
    return resistencia

# Rango de temperatura de -200°C a 200°C
temperaturas = np.linspace(-200, 200)
resistencias = pt100_resistencia(temperaturas)

# Graficar resultados
plt.plot(temperaturas, resistencias)
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohmios)')
plt.title('Comportamiento de un Sensor PT100')
plt.grid(True)
plt.show()

