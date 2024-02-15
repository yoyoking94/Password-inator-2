from tkinter import *

def entry(passwordPreview):
    entryWidget = Entry(passwordPreview, font=('Helvetica', 15), bg='#f6a522', fg='#000')
    entryWidget.grid(pady=25, padx=5, row=1, column=2)
    return entryWidget
