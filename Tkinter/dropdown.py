# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:18:36 2020

@author: luan9
"""




from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog



root = Tk()
root.title('Learn to Code at Codemy.com')
root.tk.call('tk', 'scaling', 4.0)
root.geometry("400x400")

def show():
    myLabel = Label(root, text= clicked.get()).pack()

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="show selection", command = show).pack()

root.mainloop()