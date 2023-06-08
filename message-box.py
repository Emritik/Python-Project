from tkinter import *
from tkinter import messagebox


def check():
    messagebox.showinfo(title='Message Box', message='warning')
    messagebox.showerror(title='error', message='something went wrong')
    messagebox.showwarning(title='warning', message='virus!!')
    print(messagebox.askretrycancel(title='Tell me', message='are you sure'))


window = Tk()
button = Button(window, text='click me', command=check)
button.pack()

window.mainloop()
