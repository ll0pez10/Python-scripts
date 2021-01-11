# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:24:07 2020

@author: luan9
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title('Learn to Code at Codemy.com')

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = "D:/Tkinter/images/", title="select a file", filetypes=(("jpeg files", "*.jpeg"),("all files", "*.*")))
    my_label = Label(root, text = root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image = my_image).pack()
    

my_btn = Button(root, text = "Open File", command = open).pack()



root.mainloop()