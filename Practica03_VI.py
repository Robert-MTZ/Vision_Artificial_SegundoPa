# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:44:03 2024

@author: Roberto Martinez Bailon 21310216
"""
import cv2
cap=cv2.VideoCapture(0)
 
 
while True:
    f,frame=cap.read()
    frame=cv2.Canny(frame,50,100)
    if f==True:
        cv2.imshow("canny",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


