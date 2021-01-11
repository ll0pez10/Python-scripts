# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:47:47 2020

@author: luan9
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog



root = Tk()
root.title('Learn to Code at Codemy.com')
root.geometry("400x400")

def slide(var):
    my_label= Label(root, text= horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=0, to = 200)
vertical.pack()

horizontal = Scale(root, from_=0, to = 400, orient = HORIZONTAL, command = slide)
horizontal.pack()

my_label= Label(root, text= horizontal.get()).pack()

my_btn = Button(root, text="Click Me!", command = slide).pack()


root.mainloop()
