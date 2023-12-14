#!python3

"""
Binding events to anywhere in the program

An event doesn't need to be bound just to a widget. You can bind
it to the window.  This is what allows us to create hotkeys
or global events
"""

import tkinter as tk 
from tkinter import *

def myfunc(e):
    e1.insert(0,"F1 pressed")
    print("F1 pressed")


win = tk.Tk()
win.geometry("300x200")

#Note that this binding is made to the window, not a specific widget
win.bind("<F1>",myfunc)
e1 = Entry(win,width=200)
e1.pack()
win.mainloop()