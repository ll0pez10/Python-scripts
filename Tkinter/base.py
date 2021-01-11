# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:11:45 2020

@author: luan9
"""


from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Learn to Code at Codemy.com')

def open():
    global my_img
    
    top = Toplevel()
    top.title('Praticando codigo')
    #lbl = Label(top, text = "Hello World!").pack()

    my_img = ImageTk.PhotoImage(Image.open("D:/Tkinter/images/aspen.png"))
    my_label = Label(top, image=my_img).pack()
    
    btn2 = Button(top, text="close window", command = top.destroy).pack()
    


btn = Button(root, text="Open Second Window", command = open).pack()



root.mainloop()