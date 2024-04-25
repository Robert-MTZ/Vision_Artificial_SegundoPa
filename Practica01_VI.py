# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:25:10 2024

@author: Roberto Martinez Bailon
"""

import cv2 
import numpy as np
imagen=cv2.imread("Ladrillos.jpg",0)
kernel=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

m,n=imagen.shape
filtrada=np.zeros_like(imagen)

for x in range(m-2):
    for y in range(n-2):
      res=np.sum(imagen[x:x+3,y:y+3]*kernel)
      if abs(res)>50:
           filtrada[x,y]=255
          # print(res)
        
cv2.imshow("imagen original",imagen)
cv2.imshow("imagen filtrada",filtrada)
cv2.waitKey()
cv2.destroyAllWindows()





