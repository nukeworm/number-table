#!/usr/bin/env python
from tkinter import *


# backend calculation
def printTable():
    num = int(entry.get())
    res = "\n\n"
    for i in range(1,11):
        res = res + str(num) + " x " + str(i) + " = " + str(i*num) + "\n"
    text.set(res)


# create object of tkinter
root = Tk()

# create description label
Label(root, text="Enter Number: ").pack()

# create entry box to take input
entry = Entry(root, bg="white")
entry.pack()

# create button to display output
Button(root, text="Print Table", command=printTable).pack()

# variable to display
text = StringVar()
text.set("--")

# label where output is displayed
Label(root, textvariable=text).pack()

root.mainloop()
