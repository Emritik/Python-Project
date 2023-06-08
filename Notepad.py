from tkinter import *
from tkinter import filedialog
import os

window = Tk()
def open():
    filepath = filedialog.askopenfilename()
    if filepath:

        with open(filepath,'r') as file:

            content = file.read()
            text_area.delete(1.0,END)
            text_area.insert(END,content)




def  save():
    file_name = filedialog.asksaveasfilename(defaultextension='.txt',
                                    filetypes=[
                                        ('Text file', '.txt'),
                                        ('HTML file', '.html'),
                                        ('All file', '.*')
                                    ])


window.title('Notepad')
menubar = Menu(window)
window.config(menu=menubar)
#filemenu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label='New Window')
filemenu.add_command(label='Open', command=open)
filemenu.add_command(label='Save', command=save)
filemenu.add_command(label='Save As', command=save)
filemenu.add_separator()
filemenu.add_command(label='page steup...')
filemenu.add_command(label='Print')
filemenu.add_separator()
filemenu.add_command(label='Exit')
#editmenu
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
#formatmenu
formatmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Format', menu=formatmenu)
formatmenu.add_command(label='Word Wrap')
formatmenu.add_command(label='Font...')
#Viewmenu
viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Zoom')
viewmenu.add_command(label='Status Bar')
#helpmenu
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='View Help')
helpmenu.add_command(label='Send Feedback')
helpmenu.add_separator()
helpmenu.add_command(label='About Notepad')
text_area = Text(window, width=200,
     height=80,
     font=('Times new roman', 14)).pack()


window.geometry('1000x500')
window.mainloop()
