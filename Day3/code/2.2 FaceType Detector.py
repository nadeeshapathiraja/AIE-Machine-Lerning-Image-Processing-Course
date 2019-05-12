import pickle

train_data=pickle.load(open('train_data.pickle','rb'))
train_target=pickle.load(open('train_target.pickle','rb'))

def Predict_face(points,shape):

    face_dict={'0':Diamond,'1':Oblong,'2':Oval,'3':Round,'4':Square,'5':Triangle}
    
    my_points=points[2:9,0]#Assign point 1to point 9 to my_points# awagema 0 dala x value aka pamanak use karai

    d1=my_points[6]-my_points[0]
    d2=my_points[6]-my_points[1]
    d3=my_points[6]-my_points[2]
    d4=my_points[6]-my_points[3]
    d5=my_points[6]-my_points[4]
    d6=my_points[6]-my_points[5]

    D1=d2/float(d1)*100
    D2=d3/float(d2)*100
    D3=d4/float(d3)*100
    D4=d5/float(d4)*100
    D5=d6/float(d5)*100

    result=clsfr.predict([D1,D2,D3,D4,D5])

    result=result[0]

    cv2.putText(img,face_dict[result],[100,100],cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),3)
    cv2.imshow('Live',img)


#print(train_data)
#print(train_target)

from sklearn.neighbors import KNeighborsClassifier #load KNN classifire

clsfr= KNeighborsClassifier(n_neighbors=3)# create object clsfr and use n_neighbors value for K

clsfr.fit(train_data,train_target)#use fit for tarin machine


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

    Predict_face(points)
