from tkinter import *


def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print('you ordered: ')
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window, bg='#f7ff88',
                  fg='#000',
                  font=('Constantia', 30),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()
button = Button(window, text='submit', command=submit)
listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "hotdog")
listbox.insert(4, "garlic bread")
listbox.insert(5, "burger")
entryBox = Entry(window)
addbutton = Button(window, text='Add', command=add)
deletebutton = Button(window, text='Delete', command=delete)
entryBox.pack()
button.pack()
addbutton.pack()
deletebutton.pack()
window.mainloop()
