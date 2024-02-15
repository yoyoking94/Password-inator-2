from tkinter import *

## ==== Import frontend ==== ##
## ==== Import backend ==== ##
from Backend import encrypt
from Backend import decrypt

def createNavbar(root):
    navbar = Menu(root)
    file = Menu(navbar, tearoff=0)
    file.add_command(label='Encrypt file', command=encrypt.encrypt)
    file.add_command(label='Decrypt file', command=decrypt.decrypt)
    file.add_separator()
    file.add_command(label='Quit', command=root.quit)
    navbar.add_cascade(label='File', menu=file)
    root.config(menu=navbar)