import numpy as np
import matplotlib.pyplot as plt

def carga_descarga(t, V, R, C):
    """
    Ecuación de carga y descarga para un circuito RC.
    t: tiempo
    V: voltaje inicial
    R: resistencia
    C: capacitancia
    """
    tau = R * C
    V_carga = V * (1 - np.exp(-t / tau))
    V_descarga = V * np.exp(-t / tau)
    return V_carga, V_descarga

# Obtener datos del usuario
V = float(input("Ingrese el voltaje inicial (V): "))
R = float(input("Ingrese la resistencia (Ω): "))
C = float(input("Ingrese la capacitancia (μF): "))

# Crear datos de tiempo
t = np.linspace(0, 5 * R * C, 1000)

# Calcular voltajes de carga y descarga
V_carga, V_descarga = carga_descarga(t, V, R, C)

# Graficar resultados
plt.plot(t, V_carga, label='Carga')
plt.plot(t, V_descarga, label='Descarga')
plt.xlabel('Tiempo')
plt.ylabel('Voltaje')
plt.title('Carga y Descarga en un Circuito RC')
plt.legend()
plt.grid(True)
plt.show()
