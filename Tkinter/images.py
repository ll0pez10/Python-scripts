# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:06:08 2020

@author: luan9
"""


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code at codemy.com')
#root.iconbitmap('D:')

my_img = ImageTk.PhotoImage(Image.open("D:/Tkinter/images/aspen.png"))
my_label = Label(image = my_img)
my_label.pack()


button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()


root.mainloop()