
import cv2
import numpy as np

#setup
img1 = np.zeros((400,600), dtype=np.uint8)
img1[100:300,200:400] = 255
img2 = np.zeros((400,600), dtype=np.uint8)
img2 = cv2.circle(img2,(300,200),125,(255),-1)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#and
img1 = np.zeros((400,600), dtype=np.uint8)
img1[100:300,200:400] = 255
img2 = np.zeros((400,600), dtype=np.uint8)
img2 = cv2.circle(img2,(300,200),125,(255),-1)
AND = cv2.bitwise_and(img1,img2)
cv2.imshow('AND', AND)
cv2.imwrite('AND.jpg', AND)
cv2.waitKey(0)
cv2.destroyAllWindows()
#not
img1 = np.zeros((400,600), dtype=np.uint8)
img1[100:300,200:400] = 255
img2 = np.zeros((400,600), dtype=np.uint8)
img2 = cv2.circle(img2,(300,200),125,(255),-1)
NOT = cv2.bitwise_not(img1)
cv2.imshow('NOT', NOT)
cv2.imwrite('NOT.jpg', NOT)
cv2.waitKey(0)
cv2.destroyAllWindows()
#or
img1 = np.zeros((400,600), dtype=np.uint8)
img1[100:300,200:400] = 255
img2 = np.zeros((400,600), dtype=np.uint8)
img2 = cv2.circle(img2,(300,200),125,(255),-1)
OR = cv2.bitwise_or(img1,img2)
cv2.imshow('OR', OR)
cv2.imwrite('OR.jpg', OR)
cv2.waitKey(0)
cv2.destroyAllWindows()

