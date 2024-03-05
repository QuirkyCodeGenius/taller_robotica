import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen del logo (asegúrate de tener la imagen en tu directorio de trabajo)

image_path =  "C:/Users/Familia/electivaRobotica/fotos/images.jpg"
logo_image = cv2.imread(image_path)

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(logo_image, cv2.COLOR_BGR2GRAY)

# Aplicar umbral para obtener una imagen binaria
_, thresh = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

# Encontrar contornos en la imagen binaria
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una imagen en blanco para dibujar los contornos
contour_image = np.zeros_like(logo_image)

# Dibujar los contornos en la imagen en blanco
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Mostrar la imagen original y la imagen con los contornos
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(logo_image, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
plt.title('Contornos')

plt.show()

# Imprimir las coordenadas X y Y de los contornos
for contour in contours:
    for point in contour:
        x, y = point[0]
        print(f'Coordenadas: X={x}, Y={y}')
