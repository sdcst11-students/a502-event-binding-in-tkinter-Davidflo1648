#!python3
"""
Use the StrinVar.set() method to change the value of a variable to be used
in a Label widget!
"""

import tkinter as tk 
from tkinter import *

win = tk.Tk()

# variables to be used in Tkinter widgets don't follow the standard syntax
# that we developed with basic Python programming
# We need to first create the variable and use new data types
labelData = StringVar()

# Note that we can also use an IntVar as an option, although this is
# primarily for widgets that need to return a numerical value like a
# scrollbar  or slider.  In most circumstances, it's probably best to
# use a StringVar() and convert it to a float or int as necessary
# see example2.py
e2IntData = IntVar()

# To make the contents of a label or entry dynamic, we can use the
# option "textvariable" instead of "text".
# text creates a set text content, whereas textvariable will display
# the contents of a variable, and update the contents as soon as the
# variable contents changes.
e1 = Entry(win,width=15)
l1 = Label(win, width=15, textvariable=labelData)
e2 = Entry(win, width=5)
# Then, instead of using the regular variable assignment, we use a method
# to set the contents of the variable
labelData.set("Label Contents")


e1.pack()
l1.pack()
e2.pack()
win.mainloop()