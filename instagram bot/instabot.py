import tkinter
from tkinter import*
#import tkMessageBox
top = tkinter.Tk()
# Code to add widgets will go here...
def helloCallBack():
    C = tkinter.Canvas(top, bg="blue", height=250, width=300)

    coord = 10, 50, 240, 210
    arc = C.create_arc(coord, start=0, extent=150, fill="red")

    C.pack()
#  tkMessageBox.showinfo( "Hello Python", "Hello World")
def enter():
    L1 = Label(top, text="User Name")
    L1.pack( side = LEFT)
    E1 = Entry(top, bd =5)
    E1.pack(side = RIGHT)

B = tkinter.Button(top, text ="Hello", command = helloCallBack)
c = tkinter.Button(top, text ="enter", command = enter)
B.pack()
c.pack()
top.mainloop()