#!/usr/bin/env python3
from tkinter import Tk, Canvas, PhotoImage

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WIDTH = 200
HEIGHT = 224


window = Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50)

canvas = Canvas(width=WIDTH, height=HEIGHT)
img = PhotoImage(file='tomato.png')
canvas.create_image(WIDTH/2 + 3, HEIGHT/2, image=img)
canvas.pack()

window.mainloop()
