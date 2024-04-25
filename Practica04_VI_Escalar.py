import cv2

image = cv2.imread('Ladrillos.jpg')

# Escalando una imagen
imageOut = cv2.resize(image,(600,300), interpolation=cv2.INTER_CUBIC)

cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen de salida',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()