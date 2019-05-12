import cv2#opencv
img=cv2.imread('Samples 1/flower.jpg')#load Image

#cv2.imshow('Img',img)##display Image

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

'''rgb= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('rgb',rgb)
hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
'''
import numpy as np
for i in range (0,100):
    x=np.random.randint(0,300)
    y=np.random.randint(0,300)

    gray[x,x]=255


blur=cv2.blur(gray,(3,3))
cv2.imshow('BLUR',blur)

from matplotlib import pyplot as plt
'''
plt.subplot(211)
plt.imshow(gray[100:110,100:150],cmap='binary')
plt.subplot(212)
plt.imshow(blur[100:110,100:150],cmap='binary')
'''
plt.show()


