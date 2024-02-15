from tkinter import *

## ==== Import backend ==== ##
from Backend import password

def updatePassword(entryPassword, array):
    entryPassword.delete(0, END)
    entryPassword.insert(0, password.password(array))
    
    