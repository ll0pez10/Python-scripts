# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:37:59 2020

@author: luan9
"""

import requests
import json
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Codemy.com - Learn to Code!')
root.geometry("600x100")

def graph():
    house_prices = np.random.normal(200000, 2500, 5000)
    plt.hist(house_prices, 50)
    plt.show()

my_button = Button(root, text = "Graph It!", command = graph)
my_button.pack()

root.mainloop()