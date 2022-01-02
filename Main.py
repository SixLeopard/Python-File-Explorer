#!/usr/bin/python

import os
import tkinter as tk
from tkinter import Scrollbar, Toplevel, ttk
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
    Files = []
    counter = 0
    filecounter = 0
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
            Files.append(path + locations)
            buttons.append(tk.Button(master = root, text=filelocations, command=lambda filecounter=filecounter: OpenFile(Files[filecounter], root)))
            filecounter += 1
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
    
    def OpenFile(path, root):
        f = open(path, "r")
        FileWindow = Toplevel(root)
        FileWindow.grid_columnconfigure(0, weight=1)
        FileWindow.grid_rowconfigure(0, weight=1)
        Content = tk.Text(FileWindow)
        Content.grid(row=0, column=0, sticky='ewns')
        Content.insert(tk.END, f.read())
        Scrollbar = tk.Scrollbar(FileWindow, orient="vertical", command=Content.yview)
        Scrollbar.grid(row=0, column=1, sticky='ns')
        Scrollbar.config(command=Content.yview)
        Content.config(yscrollcommand = Scrollbar.set)

    #Clear = tk.Button(master = root, text="clear", command=clears)
    #Clear.pack()

list(path, root)







root.mainloop()