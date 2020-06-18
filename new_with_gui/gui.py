import os
import sys
#import tkinter.messagebox as tkMessageBox
from tkinter import *
import tkinter.messagebox as messagebox


top = Tk()
top.title('Wel-Come to Gate Recognition System')

def start():
    top.destroy()
    os.system("python start.py")

def exit():
    top.destroy()
    



map = PhotoImage(file='back.png')
exit1 = PhotoImage(file='exit1.png')




C = Canvas(width=1280, height=720, bg='#282E40') #background
C.create_image(0, 0, image=map, anchor=NW)
C.pack(expand=YES, fill=BOTH)



B1 = Button(top,command = start ,text = "START",font=("Helvetica", 36,"bold"),activebackground ="#181818",bg = "#282E40",fg = "white",height = 2, width= 7) #image = path text = "User Login",  font = "times,bold",activebackground ="skyblue",bg = "black",fg = "white",height = 5 , width= 20
B1.place(x = 400 , y = 250) #position
B2 = Button(top,command = exit,image = exit1) 
B2.place(x = 400 , y = 470)




top.geometry("1280x720")   #display size
top.config(bg="#254070")   #display background
top.mainloop()
