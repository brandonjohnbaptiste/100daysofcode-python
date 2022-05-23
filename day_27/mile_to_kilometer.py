from math import floor
from tkinter import Tk, Entry, Label, Button, StringVar


kilometer = 0
arial = ('Arial', 15, 'normal')


def calculate_kilometer(mile):
    global kilometer
    kilometer = floor(float(mile) * 1.609)


window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

miles = StringVar()

txt_input = Entry(window, textvariable=miles, width=10)
miles_label = Label(window, text='Miles', font=arial)
equal_to = Label(window, text='is equal to', font=arial)
kilometer_display = Label(window, text=kilometer, font=arial)
kilometer_label = Label(window, text='Km', font=arial)
btn = Button(window, text='Calculate', command=lambda: calculate_kilometer(miles.get()))

txt_input.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
equal_to.grid(column=0, row=1)
kilometer_display.grid(column=1, row=1)
kilometer_label.grid(column=2, row=1)
btn.grid(column=1, row=2)


window.mainloop()
