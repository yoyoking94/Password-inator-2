import os
from tkinter import *

## ==== Import frontend ==== ##
from Frontend import displayFrame
from Frontend import navbar
## ==== Import backend ==== ##
from Backend import key

def appFrame():
    root = Tk()
    root.title('Password-inator')
    root.geometry('1080x720')
    root.minsize(1080, 720)
    root.maxsize(1920, 1080)
    root.iconbitmap('S:\Project\Python\Password-inator\Mark II\Assets\logo.ico')
    root.config(background='#f6a522')
    
    navbar.createNavbar(root)
    displayFrame.displayFrame(root)

    root.mainloop()