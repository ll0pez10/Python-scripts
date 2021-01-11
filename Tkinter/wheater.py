# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 07:47:00 2020

@author: luan9
"""

import requests
import json
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3

root = Tk()
root.title('Codemy.com - Learn to Code!')
root.geometry("600x100")

#Create Zipcode Lookup function

def zipLookup():
    #zip.get()
    #zipLabel = Label(root, text=zip.get())
    #zipLabel.grid(row = 1, column = 0, columnspan=2)
    
    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip.get()+"&distance=25&API_KEY=767C0E4B-0844-4CF3-97F5-A79A2D98A573")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
    
        if category == "Good":
            weather_color = "#00e400"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "##ff7e00"
        elif category == "Unhealthy":
            weather_color = "#167fac"
        elif category == "Very Unhealthy":
            weather_color = "#ff0000"
        elif category == "Hazardous":
            weather_color = "#99004c"
    
        myLabel = Label(root, text = city + " Air Quality " + str(quality) + " " + category, font = ("Helvetica", 12), background = weather_color)
        root.configure(background = weather_color)
        myLabel.grid(row = 1,column = 0, columnspan = 2)
    
    except Exception as e:
        api = "Error..."


zip = Entry(root)
zip.grid(row = 0, column = 0, stick = W+E+N+S)

zipButton = Button(root, text = "Lookup Zipcode", command = zipLookup)
zipButton.grid(row = 0, column = 1, stick = W+E+N+S)


root.mainloop()