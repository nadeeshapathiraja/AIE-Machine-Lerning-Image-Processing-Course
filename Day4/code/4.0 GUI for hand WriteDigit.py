import tkinter as tk
from PIL import ImageTk, Image, ImageDraw

#import PIL
import cv2
import numpy as np

import os#for connect os and create/delete/view/access folde of files

#import matplotlib as plt

try:
    os.mkdir('data')

except:
    print('Path Already Exisit')


win=tk.Tk()
width=500
height=500

count=0

from sklearn import datasets

digits =datasets.load_digits()

data=digits.data
target=digits.target

from sklearn import svm

clsfr=svm.SVC(kernel='linear')

clsfr.fit(data,target)

def event_function(event):

    x=event.x
    y=event.y
    #lable_predict.config(text=str(x)+','+str(y))

    x1=x-20
    y1=y-20
    x2=x+20
    y2=y+20
    canvas.create_oval((x1,y1,x2,y2),fill='black')
    img_draw.ellipse((x1,y1,x2,y2),fill='white')

def save():

    global count
    
    img_array=np.array(img)
    img_array=cv2.resize(img_array,(8,8))

    path=os.path.join('data',str(count)+'.jpg')#path=data/0.jpg

    cv2.imwrite(path,img_array)
    count=count+1

def clear():
    global img,img_draw

    canvas.delete('all')
    img=Image.new('RGB',(width,height),(0,0,0))
    img_draw=ImageDraw.Draw(img)

def predict():

    img_array=np.array(img)#convert to numpy array
    img_array=cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)#conver to gray imagr
    img_array=cv2.resize(img_array,(8,8))

   # plt.imshow(img_array,cmap='Binary')

    img_array=np.reshape(img_array,(1,64))#reshape array

    img_array=img_array*15.0/255.0

    result=clsfr.predict(img_array)

    lable_predict.config(text='PREDICTED DIGIT: '+ str(result))
    #plt.show()

    

font_button='Helvetica 20 bold'

canvas= tk.Canvas(win,width=width,height=height, bg='white')
#create canvers
canvas.grid(row=0,column=0,columnspan=4)

button_save=tk.Button(win,text='SAVE',bg='green',font=font_button,command=save)
button_save.grid(row=1,column=0, padx=4)#padx pady use to fixing space

button_predict=tk.Button(win,text='PREDICT',bg='blue',font=font_button, command=predict)
button_predict.grid(row=1,column=1)

button_clear=tk.Button(win,text='CLEAR',bg='yellow',font=font_button, command=clear)
button_clear.grid(row=1,column=2)

button_exit=tk.Button(win,text='EXIT',bg='red',font=font_button, command=win.destroy)
button_exit.grid(row=1,column=3)

lable_predict=tk.Label(win, text='PREDICTED DIGIT: NONE',bg='gray90',font=font_button)
lable_predict.grid(row=2,column=0,columnspan=4)


canvas.bind('<B1-Motion>',event_function)


img=Image.new('RGB',(width,height),(0,0,0))
img_draw=ImageDraw.Draw(img)#can drow in image

win.mainloop()


