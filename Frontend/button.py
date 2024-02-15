from tkinter import Button

def button(frame, text, command, column):
    button = Button(frame, text=text, font=('Helvetica', 15), bg='#f6a522', fg='#000', command=command)
    button.grid(pady=25, padx=5, row=1, column=column)
    return button
