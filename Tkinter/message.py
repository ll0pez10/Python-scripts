# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:59:53 2020

@author: luan9
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code at Codemy.com')

#showinfo, showwarning, showerror, askquestion, askquestion, askokcancel, askyesno

def popup():
    #messagebox.showinfo("This is my Popup!", "Hello World!")
    response = messagebox.askokcancel("This is my Popup!", "Hello world!")
    Label(root, text = response).pack()
    #if response == 1:
    #    Label(root, text = "You clicked yes!").pack()
    #else:
    #    Label(root, text = "You clicked no!").pack()

Button(root, text ="Popup", command = popup).pack()



root.mainloop()