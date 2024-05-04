import cv2
import numpy as np

imagen = cv2.imread('dragon.jpg' ,0)

def roberts(imagen):
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])
    roberts_x = cv2.filter2D(imagen, -1, kernel_x)
    roberts_y = cv2.filter2D(imagen, -1, kernel_y)
    roberts_combined = cv2.addWeighted(np.abs(roberts_x), 0.5, np.abs(roberts_y), 0.5, 0)
    return roberts_combined

def sobel(imagen):
    sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combinado = cv2.addWeighted(np.abs(sobel_x), 0.5, np.abs(sobel_y), 0.5, 0)
    return sobel_combinado

def prewitt(imagen):
    kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    prewitt_x = cv2.filter2D(imagen, -1, kernel_x)
    prewitt_y = cv2.filter2D(imagen, -1, kernel_y)
    prewitt_combined = cv2.addWeighted(np.abs(prewitt_x), 0.5, np.abs(prewitt_y), 0.5, 0)
    return prewitt_combined

sobel_resultado = sobel(imagen)
prewitt_resultado = prewitt(imagen)
roberts_resultado = roberts(imagen)

cv2.imshow('Sobel',sobel_resultado)
cv2.imshow('Prewitt',prewitt_resultado)
cv2.imshow('roberts',roberts_resultado)

cv2.imwrite('Sobel.jpg',sobel_resultado)
cv2.imwrite('Prewitt.jpg',prewitt_resultado)
cv2.imwrite('roberts.jpg',roberts_resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
