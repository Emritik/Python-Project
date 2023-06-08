from tkinter import *
from tkinter import colorchooser
def click():
    color = colorchooser.askcolor()
    print(color)
    window.config(bg=color[1])
window =Tk()

button = Button(window,text='click', command=click)
button.pack()
window.geometry('420x420')

window.mainloop()