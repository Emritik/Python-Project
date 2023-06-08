from tkinter import *
def submit():
    print('The temperature is : '+str(scale.get())+' '+'Degree C.')

window = Tk()

scale = Scale(window,from_=100, to=0, length=400, tickinterval=10, fg='RED', bg='#000', troughcolor='cyan', font=('Arial',16))
scale.pack()
button = Button(window,text='submit', command=submit)
button.pack()
window.mainloop()