import cv2
import numpy as np

# Cargar imagen PNG
image = cv2.imread("slider-img.png")

# Convertir a HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definir rango de color azul a reemplazar
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

# Reemplazar azul con verde
mask = cv2.inRange(hsv, lower_blue, upper_blue)
hsv[mask > 0] = (60, 255, 255)  # Verde en HSV

# Convertir de vuelta a RGB
new_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Guardar nueva imagen
cv2.imwrite("imagen_verde.png", new_image)
