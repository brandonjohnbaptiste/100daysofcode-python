#!/usr/bin/env python3
from tkinter import Tk, Label, Button, Entry, StringVar


def button_clicked():
    text_label["text"] = user_msg.get()
    user_msg.set('')


window = Tk()
window.title('I clicked a button!')
window.minsize(width=500, height=800)

text_label = Label(window, text="Click that button!", font=("Arial", 30, "normal"))
user_msg = StringVar()
text_input = Entry(window, textvariable=user_msg, width=30)
btn = Button(window, text='Click me', command=button_clicked)

text_label.pack()
text_input.pack()
btn.pack()

window.mainloop()

