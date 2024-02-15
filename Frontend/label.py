from tkinter import Label

def label(passwordPreview, text):
    Label(passwordPreview, text=text, font=('Helvetica', 15), bg='#f6a522', fg='#000').grid(pady=25, padx=5, row=1, column=1)