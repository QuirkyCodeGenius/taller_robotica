import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Pedir al usuario las coordenadas del vector
x = float(input('Ingrese la coordenada X del vector: '))
y = float(input('Ingrese la coordenada Y del vector: '))
z = float(input('Ingrese la coordenada Z del vector: '))

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar el sistema de coordenadas
ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='X')
ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='Y')
ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='Z')

# Dibujar el vector ingresado por el usuario
ax.quiver(0, 0, 0, x, y, z, color='orange', label='Vector')

# Configurar el aspecto del gráfico
ax.set_xlim([0, max(1, abs(x), abs(y), abs(z))])
ax.set_ylim([0, max(1, abs(x), abs(y), abs(z))])
ax.set_zlim([0, max(1, abs(x), abs(y), abs(z))])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Mostrar el gráfico
plt.show()
