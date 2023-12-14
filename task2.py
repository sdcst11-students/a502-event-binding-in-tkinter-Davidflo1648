#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import math
from tkinter import Tk, Label, Entry, Button, StringVar

win=Tk()
win.title('Hypotenuse Calculator')
win.geometry('550x100')

hyp = StringVar()
hyp.set('Hypotenuse')

def hyp_calc():
    side1 = side1_entry.get()
    side2 = side2_entry.get()
    hyp.set(math.hypot(side1,side2))

instruction_label = Label(win,text='Only for Right Triangles!')
side1_label = Label(win,text='Enter side:')
side1_entry = Entry(win)
side2_label = Label(win,text='Enter other side:')
side2_entry = Entry(win)
calc_button = Button(win,text='Calculate Hypotenuse',command=hyp_calc)
hyp_label = Label(win,text='Hypotenuse')
hyp_entry = Entry(win, width=20, textvariable=hyp)

instruction_label.grid(row=1,column=3)
side1_label.grid(row=2,column=1)
side1_entry.grid(row=2,column=2)
side2_label.grid(row=2,column=4)
side2_entry.grid(row=2,column=5)
calc_button.grid(row=3,column=3)
hyp_label.grid(row=4,column=1)
hyp_entry.grid(row=4,column=2)

win.mainloop()