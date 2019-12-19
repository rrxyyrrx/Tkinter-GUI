import tkinter as tk
from tkinter.colorchooser import *

root = tk.Tk()

#minimum size

root.minsize(width = 600, height = 500)


#Widgets Functions

def clrClicked():
    color = askcolor()
    print(color)

#Create a class for getting a color, maybe a frame that has all buttons in it, row1 coloumn 1. 1Xamount buttons
#Change the 'print color' color variable into list from tuple. Remove the extra values


#button1 = tk.button(root, 

text_area = tk.Text(root, height=6)
text_area.grid(row = 3, column = 3, rowspan = 5, columnspan = 6, sticky="S")

label1 = tk.Label(root, text="Text Edit")
label1.grid(row=0, column=4)

label2 = tk.Label(root, text="Utilities")
label2.grid(row=2, column=2)

buttonClr = tk.Button(root, text = "Color", command = clrClicked, bg="black", fg="red")
buttonClr.grid(row = 2, column = 3)

#End Widgets

root.title("Text Editor Madness")

root.mainloop()

