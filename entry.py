from tkinter import *

window = Tk()
window.title("bu command")

entry = Entry(window,width=50, bg="blue", fg="white")
entry.insert(0, " enter ur name: ")
entry.pack()


def click():
    hello = "hello" + entry.get()
    l1 = Label(window, text=hello)
    l1.pack()


button = Button(window, text="enter ur name", command=click)
button.pack()



window.mainloop()
