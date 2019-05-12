import cv2 #open computer vision for image processing tasks

camera=cv2.VideoCapture(0) # Loding the default(0) camera into camera object

import dlib

face_detector=dlib.get_frontal_face_detector()
#loding face ditector for detect face it is a klibrary in dlib

landmarks_detector=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#loading the 68 landmarks detecting classifire intp]o landmarks

import imutils
from imutils import face_utils


while(True):

    ret,img= camera.read()#reading one frame camera and assign in to img // ret is not use it disply camera on or off
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert to rgb to gray color
    #cv2.imshow('Live',gray)

    rect= face_detector(gray)

    #x1=rect[0].left()
    #y1=rect[0].top()
    #x2=rect[0].right()
    #y2=rect[0].bottom()

    #cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

    points = landmarks_detector(gray,rect[0])#reciving 68 pointsto face point object

    points=face_utils.shape_to_np(points)#converting the points into numpy array


    for p in points:
        cv2.circle(img,(p[0],p[1]),2,(0,0,255),)
    
    
    cv2.imshow('LIVE1',img)
    cv2.waitKey(1)# 1ms delay
