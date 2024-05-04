import cv2
import numpy as np

# Función para agregar ruido gaussiano a una imagen
def ruido_gaussiano(imagen, mean=0, sigma=25):
    row, col, ch = imagen.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    noisy = np.clip(imagen + gauss, 0, 255)
    return noisy.astype(np.uint8)


# Función para agregar ruido de sal y pimienta a una imagen
def ruido_sal_pimienta(imagen, cantidad=0.05):
    imagen_copia = imagen
    filas, columnas, _ = imagen_copia.shape
    num_sal = np.ceil(cantidad * imagen_copia.size * 0.5)
    num_pimienta = np.ceil(cantidad * imagen_copia.size * 0.5)
    
    # Sal
    coords_sal = [np.random.randint(0, i - 1, int(num_sal)) for i in imagen_copia.shape]
    imagen_copia[coords_sal[0], coords_sal[1], :] = 255

    # Pimienta
    coords_pimienta = [np.random.randint(0, i - 1, int(num_pimienta)) for i in imagen_copia.shape]
    imagen_copia[coords_pimienta[0], coords_pimienta[1], :] = 0
    return imagen_copia

# Cargar imagen
image = cv2.imread('squirtle.jpg')

# Añadir ruido 
imagen_ruido_gaus = ruido_gaussiano(image)
imagen_sal_pimienta = ruido_sal_pimienta(image)

# Funciones para aplicar filtros
def filtro_gaussiano(imagen):
    return cv2.GaussianBlur(imagen, (5, 5), 0)

def filtro_media(imagen):
    return cv2.blur(imagen, (5, 5))

def filtro_mediana(imagen):
    return cv2.medianBlur(imagen, 5)

def filtro_minimo(imagen):
    return cv2.erode(imagen, np.ones((5, 5), np.uint8))

def filtro_maximo(imagen):
    return cv2.dilate(imagen, np.ones((5, 5), np.uint8))

#Aplicamos filtros a la imagen con ruido gausss
ruido_gaus_filtro_gaus = filtro_gaussiano(imagen_ruido_gaus)
ruido_gaus_filtro_media = filtro_media(imagen_ruido_gaus)
ruido_gaus_filtro_mediana = filtro_mediana(imagen_ruido_gaus)
ruido_gaus_filtro_minimo = filtro_minimo(imagen_ruido_gaus)
ruido_gaus_filtro_maximo = filtro_maximo(imagen_ruido_gaus)

#Aplicamos filtros a imagenes con ruido sal y pimienta
ruido_SP_filtro_gaus = filtro_gaussiano(imagen_sal_pimienta)
ruido_SP_filtro_media = filtro_media(imagen_sal_pimienta)
ruido_SP_filtro_mediana = filtro_mediana(imagen_sal_pimienta)
ruido_SP_filtro_minimo = filtro_minimo(imagen_sal_pimienta)
ruido_SP_filtro_maximo = filtro_maximo(imagen_sal_pimienta)


# Mostrar resultados
imagen = cv2.imread('squirtle.jpg')
cv2.imshow('Imagen Original',imagen)
cv2.imshow('imagen con Ruido Gaussian', imagen_ruido_gaus)
cv2.imshow('imagen con Ruido Sal y Pimienta', imagen_sal_pimienta)
cv2.waitKey(0)
cv2.imshow('imagen con Ruido Gaussiano con Filtro Gauss', ruido_gaus_filtro_gaus)
cv2.imshow('imagen con Ruido Gaussiano con Filtro Media', ruido_gaus_filtro_media)
cv2.imshow('imagen con Ruido Gaussiano con Filtro Mediana', ruido_gaus_filtro_mediana)
cv2.imshow('imagen con Ruido Gaussiano con Filtro Minimo', ruido_gaus_filtro_minimo)
cv2.imshow('imagen con Ruido Gaussiano con Filtro Maximo', ruido_gaus_filtro_maximo)

cv2.waitKey(0)
cv2.imshow('imagen con Ruido S&P con Filtro Gauss', ruido_SP_filtro_gaus)
cv2.imshow('imagen con Ruido S&P con Filtro Media', ruido_SP_filtro_media)
cv2.imshow('imagen con Ruido S&P con Filtro Mediana', ruido_SP_filtro_mediana)
cv2.imshow('imagen con Ruido S&P con Filtro Minimo', ruido_SP_filtro_minimo)
cv2.imshow('imagen con Ruido S&P con Filtro Maximo', ruido_SP_filtro_maximo)

#Se Guardan las imagenes
cv2.imwrite('imagen con Ruido Gaussiano.jpg',imagen_ruido_gaus)
cv2.imwrite('imagen Ruido Gaussiano con Filtro Gauss.jpg', ruido_gaus_filtro_gaus)
cv2.imwrite('imagen Ruido Gaussiano con Filtro Media.jpg', ruido_gaus_filtro_media)
cv2.imwrite('imagen Ruido Gaussiano con Filtro Mediana.jpg', ruido_gaus_filtro_mediana)
cv2.imwrite('imagen Ruido Gaussiano con Filtro Minimo.jpg', ruido_gaus_filtro_minimo)
cv2.imwrite('imagen Ruido Gaussiano con Filtro Maximo.jpg', ruido_gaus_filtro_maximo)

cv2.imwrite('imagen con Ruido Sal y Pimienta.jpg', imagen_sal_pimienta)
cv2.imwrite('imagen con Ruido S&P con Filtro Gauss.jpg', ruido_SP_filtro_gaus)
cv2.imwrite('imagen con Ruido S&P con Filtro Media.jpg', ruido_SP_filtro_media)
cv2.imwrite('imagen con Ruido S&P con Filtro Mediana.jpg', ruido_SP_filtro_mediana)
cv2.imwrite('imagen con Ruido S&P con Filtro Minimo.jpg', ruido_SP_filtro_minimo)
cv2.imwrite('imagen con Ruido S&P con Filtro Maximo.jpg', ruido_SP_filtro_maximo)


cv2.waitKey(0)
cv2.destroyAllWindows()
