import cv2
import numpy as np
img= cv2.imread('Materials/light.png')#0 for gray, -1 for nochange , 1 for color

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)

contours, hierarchy= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt=contours[0]

area=cv2.contourArea(cnt)

print(area)
