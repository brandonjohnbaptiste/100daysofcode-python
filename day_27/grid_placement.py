from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title('Grid layout')

label = Label(window, text='Lorem Ipsum', font=('Arial', 30, 'normal'))
btn_1 = Button(window, text='Click me')
btn_2 = Button(window, text='Don\'t click me')
txt_input = Entry(window, width=50)

label.grid(column=0, row=0)
btn_1.grid(column=1, row=1)
btn_2.grid(column=2, row=0)
txt_input.grid(column=3, row=3)


window.mainloop()
