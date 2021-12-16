#!/usr/bin/python

import os
import tkinter as tk
from tkinter import ttk
TK_SILENCE_DEPRECATION=1

root = tk.Tk()
frame = tk.Frame(root)

path = "/"

def clear(buttons):
    for button in buttons:
        button.grid_remove()
        #print("Clearing")

def list(path, root):
    buttons = []
    directory = []
    counter = 0
    currentdir = os.listdir(path)
    column = 0
    row = 0

    updirectory = path[0:path.rfind("/")]
    #print(updirectory)
    #print(updirectory[0:updirectory.rfind("/")] + "/")
    backbutton = tk.Button(master = root, text="<--", command=lambda : ChangeDirectory(updirectory[0:updirectory.rfind("/")]+"/", root)).grid(row=row,column=column)
    column += 1

    for locations in currentdir:
        if os.path.isdir(path + locations):
            directory.append(path + locations + "/")
            buttons.append(tk.Button(master = root, text=locations + "/" ,command=lambda counter=counter: ChangeDirectory(directory[counter], root)))
            counter += 1
            #print(locations + "/" )
    #print(counter)

    #print(directory)
    for filelocations in currentdir:
        if os.path.isfile(path + filelocations):
            buttons.append(tk.Button(master = root, text=filelocations))
            #print(locations)

    for button in buttons:
        button.grid(row=row, column=column)
        row += 1
        if row == 10:
            row = 0
            column += 1

    def clears():
        clear(buttons)
    
    def ChangeDirectory(path, root):
        clear(buttons)
        print(path)
        list(path, root)
    
    #Clear = tk.Button(master = root, text="clear", command=clears)
    #Clear.pack()

list(path, root)







root.mainloop()