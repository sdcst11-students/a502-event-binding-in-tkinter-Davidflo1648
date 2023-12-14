"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
from tkinter import Tk, Label, Entry, Button, StringVar

win = Tk()
win.title('Student Info')
win.geometry('600x85')

student_info = StringVar()
student_info.set('All info')

def show_brief_info():
    name = student_name.get()
    number = student_number.get()
    grade = student_grade.get()
    student_info.set(f'{name}, {number}, {grade}')

name_label = Label(win, text='Name:')
student_name = Entry(win)
number_label = Label(win, text='Student number:')
student_number = Entry(win)
grade_label = Label(win, text='Grade:')
student_grade = Entry(win)
brief_button = Button(win, text='Brief', command=show_brief_info)
info_entry = Entry(win, width=25, textvariable=student_info)
info_label = Label(win, text='Student Info:')

name_label.grid(row=1, column=1)
student_name.grid(row=1, column=2)
number_label.grid(row=1,column=4)
student_number.grid(row=1,column=5)
grade_label.grid(row=1,column=7)
student_grade.grid(row=1,column=8)
brief_button.grid(row=2, column=1, columnspan=2)
info_label.grid(row=3, column=1)
info_entry.grid(row=3, column=2)

win.mainloop()
