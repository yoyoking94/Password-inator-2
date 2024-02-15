from tkinter import *
import os

## ==== Import frontend ==== ##
from Frontend import label
from Frontend import button
from Frontend import entry
## ==== Import backend ==== ##
from Backend import savePassword
from Backend import close

def saveFrame(entryPassword):
    root = Tk()
    root.title('Password name')
    root.geometry('675x200')
    root.iconbitmap('S:\Project\Python\Password-inator\Mark II\Assets\logo.ico')
    root.config(background='#f6a522')
    
    secondFrame = Frame(root, bg='#f6a522')
    secondFrame.pack(expand=YES)
    
    label.label(secondFrame, "Password name :")
    saveEntry = entry.entry(secondFrame)
    button.button(secondFrame, 'Save password', lambda: close.close(root, entryPassword, saveEntry), 3)
    root.mainloop()