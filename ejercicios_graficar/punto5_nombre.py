import matplotlib.pyplot as plt

# Crear una figura y ejes
fig, ax = plt.subplots()

# Definir las coordenadas para formar cada letra del nombre "Julian"
letters = {
    'J': [ (0, 0.8), (0.2, 0.8),(0.1, 0.8), (0.1, 0), (0,0), (0.1, 0)],
    'u': [(0.3, 0.8), (0.3, 0), (0.5, 0), (0.5, 0.8)],
    'l': [(0.6, 0), (0.6, 0.8), (0.6, 0), (0.8, 0)],
    'i': [(0.9, 0), (0.9, 0.8)],
    'a': [  (1, 0), (1.2, 0.8), (1.4, 0),(1.3, 0.4), (1.1, 0.4), (1.3, 0.4),],
    'n': [(1.5, 0 ), (1.5, 0.8), (1.7, 0), (1.7,0.8)],
}

# Dibujar cada letra
for letter, coordinates in letters.items():
    x, y = zip(*coordinates)
    ax.plot(x, y, label=letter)

# Configurar el aspecto del gráfico
ax.set_xlim([0, 1.5])
ax.set_ylim([0, 1])
plt.gca().set_aspect('equal', adjustable='box')  # Mantener proporciones correctas

# Mostrar el nombre de cada integrante en el gráfico
for letter, coordinates in letters.items():
    last_point = coordinates[-1]
    ax.text(last_point[0] + 0.02, last_point[1], letter, fontsize=8, verticalalignment='center')

# Añadir leyenda
ax.legend()

# Mostrar el gráfico
plt.show()
