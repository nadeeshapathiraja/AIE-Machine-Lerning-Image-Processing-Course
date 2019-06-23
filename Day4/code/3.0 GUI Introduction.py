import tkinter as tk

window = tk.Tk()#Just creating the main window

def func1():
    label1.config(text='Hellow Python',bg='blue')
    button1.config(bg='hot pink')

def func2():
    label1.config(text='Hellow World',bg='yellow')

#window.mainloop()# If not working

font1='Helvetica 20 bold'

label1=tk.Label(window,text='Submit',bg='red',fg='white',font=font1)
label1.grid(row=0,column=0)#Positioning the lable. 3Types, Grid,pick,

font2='Times 15 italic'
button1= tk.Button(window,text='Change',bg='gray20',font=font2,height=2,width=10,command=func1 )
button1.grid(row=1, column=0)

button2= tk.Button(window,text='Change',bg='green',font=font2,height=2,width=10,command=func2 )
button2.grid(row=1, column=3)
