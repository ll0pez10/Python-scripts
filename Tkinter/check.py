# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:00:49 2020

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
   myLabel = Label(root, text = var.get()).pack() 
    

var = StringVar()

c = Checkbutton(root, text = "check this box, I dare you!", variable = var, onvalue = "ON", offvalue = "OFF")
c.deselect()
c.pack()

myButton = Button(root, text = "show selection", command = show).pack()

root.mainloop()