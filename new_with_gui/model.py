import pandas as pd
from sklearn.preprocessing import StandardScaler,Normalizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import os
import sys
from tkinter import *
import tkinter.messagebox as messagebox

df=pd.read_csv("final_n.csv")

x=df.iloc[:,0:16]

obj=StandardScaler()
x1=obj.fit_transform(x)
# obj=Normalizer()
# x1=obj.fit_transform(x)


y=df['Name']

sv=LinearSVC()
sv.fit(x,y)

Xnew = pd.read_csv("test_data.csv")

# obj=StandardScaler()
# Xnew=obj.fit_transform(Xnew)

ynew = sv.predict(Xnew)

import numpy
from collections import Counter

array = numpy.array(ynew)
result = Counter(array.flat).most_common(1)

print(result)
print(array)

top = Tk()
top.title('Wel-Come to Gate Recognition System')

def restart():
    top.destroy()
    os.system("python gui.py")
    # messagebox.showinfo("Results",output)


def exit():
    top.destroy()
    



map = PhotoImage(file='back.png')
exit1 = PhotoImage(file='exit1.png')




C = Canvas(width=1280, height=720, bg='#282E40') #background
C.create_image(0, 0, image=map, anchor=NW)
C.pack(expand=YES, fill=BOTH)



B1 = Button(top,command = restart ,text = "RESTART",font=("Helvetica", 36,"bold"),activebackground ="#181818",bg = "#282E40",fg = "white",height = 2, width= 7) #image = path text = "User Login",  font = "times,bold",activebackground ="skyblue",bg = "black",fg = "white",height = 5 , width= 20
B1.place(x = 400 , y = 250) #position
B2 = Button(top,command = exit,image = exit1) 
B2.place(x = 400 , y = 470)
L = Label(top,text = result,font = ("Helvetica", 15,"bold"),activebackground ="#181818",bg = "#282E40",fg = "white",height = 10 , width= 50)  #check for the font and fontsize
L.place(x = 700 , y = 300)




top.geometry("1280x720")   #display size
top.config(bg="#254070")   #display background
top.mainloop()
