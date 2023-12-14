#!python3
"""
Assigning a function to a Button widget
Getting and Inserting Entry widgets
"""
import tkinter as tk 
from tkinter import *


win = tk.Tk()

eoutput = StringVar()
eoutput.set("Output goes here")

def clickFunction(event):
    """ 
    This function is triggered by an EVENT
    Many events can make use of the properties of an object
    that it is bound to, so the object and the event make use of 
    an input parameter. In this case, we are storing the event
    details in the variable "event"

    """
    # This command will show you some of the information about the event

    print(event)
    number = e1.get()
    number = float(number)

    answer = 2* number
    # Note...the insert method will insert output into the entry widget, with the
    # integer first parameter being the position in the Entry widget.  If there is
    # data already there, it'll confuse your output, so you need to delete the 
    # current contents
    # the Entry.delete() method takes 2 parameters, the start of the text you want
    # to delete, and the ending of the text you want to delete.  If you're not sure
    # of the length, you can delete using the special value END to go all the way
    # to the end of the entry widget
    #a_entry.delete(0,END)
    a_entry.insert(0,answer)


l1 = Label(win, text="Enter a number")
e1 = Entry(win, width=20)
b1 = Button(win, text="Click to double")
# Once we create the button widget, we can bind an event to it
# this means that when the specified action is triggered,
# the corresponding event handler function is executed
# see some of the different actions that can trigger events:
# https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
b1.bind("<Button>",clickFunction)

a_label = Label(win, text="The entry doubled is:")
a_entry = Entry(win, width=20, textvariable=eoutput)

l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
b1.grid(row=2, column=1, columnspan=2)
a_label.grid(row=3,column=1)
a_entry.grid(row=3,column=2)




win.mainloop()