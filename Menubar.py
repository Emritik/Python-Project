from tkinter import *


def openfile():
    print('file opens.')


def save():
    print('File save.')


def saveas():
    print('File save again.')


def exit():
    print('now you exit from the file.')


def cut():
    print("Cut the file.")


def copy():
    print("copied")


def paste():
    print('paste.')


window = Tk()
menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label='open', command=openfile)
filemenu.add_command(label='save', command=save)
filemenu.add_command(label='save as', command=saveas)
filemenu.add_separator()
filemenu.add_command(label='exit', command=exit)

editmenu = Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label='Cut', command=cut)
editmenu.add_command(label='Copy', command=copy)
editmenu.add_command(label='Paste', command=paste)
window.mainloop()
