# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:29:52 2020

@author: luan9
"""


from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3


root = Tk()
root.title('Learn to Code at Codemy.com')
root.tk.call('tk', 'scaling', 4.0)
root.geometry("400x400")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

#Create cursor
c = conn.cursor()

#create table
'''
c.execute(""" CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''
#create update function
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()
    
    record_id = delete_box.get()
    
    c.execute(""" UPDATE addresses SET 
              first_name = :first,
              last_name = :last,
              address = :address,
              city = :city,
              state = :state,
              zipcode = :zipcode
              
              WHERE oid = :oid""", 
              {'first': f_name_editor.get(),
               'last': l_name_editor.get(),
               'address': address_editor.get(),
               'city': city_editor.get(),
               'state': state_editor.get(),
               'zipcode': zipcode_editor.get(),
               'oid': record_id
               })

    #commit changes
    conn.commit()
    
    #close connection
    conn.close()

#create edit function to update a record
def edit():
    
    editor = Tk()
    editor.title('Learn to Code at Codemy.com')
    editor.tk.call('tk', 'scaling', 4.0)
    editor.geometry("400x200")
    
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()
    
    
    record_id = delete_box.get()
    #Query the database
    c.execute("SELECT *, oid FROM addresses WHERE oid=" + record_id)
    records = c.fetchall()
    
    #create global variables for text box names
    
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    #create text boxes
    f_name_editor = Entry(editor, width =30)
    f_name_editor.grid(row=0, column=1, padx=20, pady = (10,0))
    
    l_name_editor = Entry(editor, width =30)
    f_name_editor.grid(row=1, column=1)
    
    address_editor = Entry(editor, width =30)
    address_editor.grid(row=2, column=1)
    
    city_editor = Entry(editor, width =30)
    city_editor.grid(row=3, column=1)
    
    state_editor = Entry(editor, width =30)
    state_editor.grid(row=4, column=1)
    
    zipcode_editor = Entry(editor, width =30)
    zipcode_editor.grid(row=5, column=1)
    
    #create text box labels
    
    f_name_label_editor = Label(editor, text="First name")
    f_name_label_editor.grid(row =0, column=0, pady = (10,0))
    
    l_name_label_editor = Label(editor, text="last name")
    l_name_label_editor.grid(row =1, column=0)
    
    address_label_editor = Label(editor, text="address")
    address_label_editor.grid(row =2, column=0)
    
    city_label_editor = Label(editor, text="city")
    city_label_editor.grid(row =3, column=0)
    
    state_label_editor = Label(editor, text="state")
    state_label_editor.grid(row =4, column=0)
    
    zipcode_label_editor = Label(editor, text="zipcode")
    zipcode_label_editor.grid(row =5, column=0)
    
    #loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    
    
    
    #Create a save button
    save_btn = Button(editor, text = "Save record", command = update)
    save_btn.grid(row = 12, column = 0, columnspan =2, pady = 10, padx = 10, ipadx = 145)
    

def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()
    
    #Delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    
    #commit changes
    conn.commit()


    #Close Connection
    conn.close()


#Create Submit Function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()
    
    #Insert into Table
    
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", 
              {'f_name':f_name.get(),
               'l_name':l_name.get(),
               'address':address.get(),
               'city': city.get(),
               'state': state.get(), 
               'zipcode': zipcode.get()})
    
    #commit changes
    conn.commit()


    #Close Connection
    conn.close()
    
    #Clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
    
    
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()
    
    #Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)
    
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) +"\n"
        
    query_label = Label(root, text = print_records)
    query_label.grid(row=12, column =0, columnspan=2)    
    
    #commit changes
    conn.commit()


    #Close Connection
    conn.close()


f_name = Entry(root, width =30)
f_name.grid(row=0, column=1, padx=20, pady = (10,0))

l_name = Entry(root, width =30)
f_name.grid(row=1, column=1)

address = Entry(root, width =30)
address.grid(row=2, column=1)

city = Entry(root, width =30)
city.grid(row=3, column=1)

state = Entry(root, width =30)
state.grid(row=4, column=1)

zipcode = Entry(root, width =30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width = 30)
delete_box.grid(row = 10, column=1, pady =5)

#create text box labels

f_name_label = Label(root, text="First name")
f_name_label.grid(row =0, column=0, pady = (10,0))

l_name_label = Label(root, text="last name")
l_name_label.grid(row =1, column=0)

address_label = Label(root, text="address")
address_label.grid(row =2, column=0)

city_label = Label(root, text="city")
city_label.grid(row =3, column=0)

state_label = Label(root, text="state")
state_label.grid(row =4, column=0)

zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row =5, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row = 10, column = 0, pady = 5)

# Create Submit Button
Submit_btn = Button(root, text="Add Record to database", command = submit)
Submit_btn.grid(row=7, column =0, columnspan=2, pady=10, padx=10, ipadx=120)

#Create a Query Button
query_btn = Button(root, text = "Show records", command = query)
query_btn.grid(row = 8, column = 0, columnspan =2, pady = 10, padx = 10, ipadx = 135)

# Create a delete button
delete_btn = Button(root, text = "Delete record", command = delete)
delete_btn.grid(row = 11, column = 0, columnspan =2, pady = 10, padx = 10, ipadx = 135)

#Create an update button
update_btn = Button(root, text = "Edit record", command = edit)
update_btn.grid(row = 12, column = 0, columnspan =2, pady = 10, padx = 10, ipadx = 143)

#commit changes
conn.commit()


#Close Connection
conn.close()

root.mainloop()