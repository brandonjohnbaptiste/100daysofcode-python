#!/usr/bin/env python3
from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title('I clicked a button!')
window.minsize(width=500, height=800)

text_label = Label(text="Click that button!", font=("Arial", 30, "normal"))
text_label.pack()

text_input = Entry(width=30)
text_input.pack()


def button_clicked():
    text_label["text"] = text_input.get()


btn = Button(text='Click me', command=button_clicked)
btn.pack()

window.mainloop()

