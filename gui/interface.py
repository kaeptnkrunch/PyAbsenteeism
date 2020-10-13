from tkinter import *

from tkinter import messagebox
from datetime import date



window = Tk()

window.title("Welcome to Absenteeism Rate Calculator")

window.geometry('300x200')


def clickMe():
    label.configure(text= 'Hello ')

def clicked():

    messagebox.showinfo('Absenteeism Rate', "Answer")

currentdate=date.today()
absences=StringVar()
workingDays=StringVar()

label = Label(window, text = "Please indicate your current absences:")
label.grid(column = 0, row = 0)
name = StringVar()
nameEntered = Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 1)

label = Label(window, text = "Please now enter your current working days:")
label.grid(column = 0, row = 2)
name1 = StringVar()
nameEntered = Entry(window, width = 15, textvariable = name1)
nameEntered.grid(column = 0, row = 3)


button = Button(window, text = "calculate", command = clicked)
button.grid(column= 0, row = 4)


window.mainloop()