import cv2
import numpy as np
img= cv2.imread('Materials/light.png')#0 for gray, -1 for nochange , 1 for color

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)

contours, hierarchy= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt=contours[0]

x,y,w,h=cv2.boundingRect(cnt)

cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

rect=cv2.minAreaRect(cnt)

points=cv2.boxPoints(rect)

points= np.int0(points)
cv2.drawContours(img,[points],0,(0,0,255),2)


#circle
(x,y),radius=cv2.minEnclosingCircle(cnt)

x=int(x)
y=int(y)
radius=int(radius)

cv2.circle(img,(x,y),radius,(255,0,0),2)

#ellipse

ellipse=cv2.fitEllipse(cnt)
cv2.ellipse(img,ellipse,(0,255,255),2)



print(rect)

cv2.imshow('IMG',img)

cv2.waitKey()
