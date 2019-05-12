import cv2

img=cv2.imread('Samples 1/threshold.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thr1=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
ret,thr2=cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
ret,thr3=cv2.threshold(gray,100,255,cv2.THRESH_TRUNC)
ret,thr4=cv2.threshold(gray,100,255,cv2.THRESH_TOZERO)

cv2.imshow('img',img)
cv2.imshow('thr1',thr1)
cv2.imshow('thr2',thr2)
cv2.imshow('thr3',thr3)
cv2.imshow('thr3',thr3)
