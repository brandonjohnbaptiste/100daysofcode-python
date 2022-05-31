#!/usr/bin/env python3
from tkinter import Tk, Canvas, PhotoImage, Label, Button

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

timer_label = Label(window, text='Timer', font=(FONT_NAME, 50, 'bold'))

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
img = PhotoImage(file='tomato.png')
canvas.create_image(WIDTH/2 + 3, HEIGHT/2, image=img)
canvas.create_text(WIDTH/2, HEIGHT/2 + 20, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

start_btn = Button(window, text='Start')
reset_btn = Button(window, text='Reset')
tick_label = Label(window, text='✔')

timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)
tick_label.grid(column=1, row=3)


window.mainloop()
