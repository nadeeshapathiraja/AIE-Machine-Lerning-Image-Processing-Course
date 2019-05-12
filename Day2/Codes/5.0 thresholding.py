import cv2

img=cv2.imread('Samples 2/gray_Image.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(gray,(3,3))
ret,thr=cv2.threshold(blur,50,255,cv2.THRESH_BINARY_INV)

cv2.imshow('IMG',img)
cv2.imshow('THR',thr)
