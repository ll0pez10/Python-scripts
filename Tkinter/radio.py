# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:41:04 2020

@author: luan9
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code at Codemy.com')
#root.iconbitmap()

#r = IntVar()
#r.set("2")

MODES = [
    ("pepperoni","pepperoni"),
    ("Chesse","Chesse"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
    ]

pizza = StringVar()
pizza.set("pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable = pizza, value = mode).pack(anchor =W)


def clicked(value):
    myLabel = Label(root, text =value)
    myLabel.pack()
    

#Radiobutton(root, text="Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

#myLabel = Label(root, text =pizza.get())
#myLabel.pack()
    
myButton = Button(root, text="Click me!", command= lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
