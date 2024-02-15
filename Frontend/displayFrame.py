import os
from tkinter import *
## ==== Import frontend ==== ##
from Frontend import label
from Frontend import button
from Frontend import entry
from Frontend import checkbox
from Frontend import saveFrame
from Frontend import image
## ==== Import backend ==== ##
from Backend import updatePassword
from Backend import checked

def displayFrame(root):
    displayFrame = Frame(root, bg='#f6a522')
    displayFrame.pack(expand=YES)
    
    image.padlockImg(displayFrame, 'S:\Project\Python\Password-inator\Mark II\Assets\lock.png')
    
    passwordPreview = Frame(displayFrame, bg='#f6a522')
    passwordPreview.pack()
    
    checkboxPreview = Frame(displayFrame, bg='#f6a522')
    checkboxPreview.pack()
    
    buttonPreview = Frame(displayFrame, bg='#f6a522')
    buttonPreview.pack()
    
    label.label(passwordPreview, "Your password is :")
    entryPassword = entry.entry(passwordPreview)
    
    labels=['Include upper letters','Include lower letters','Include numbers', 'Include symbols']
    variables = []
    array = []
    for x in range(len(labels)):
        variables.append(IntVar(value=0))
        checkbox.checkbox(checkboxPreview, labels, variables, x, array)
    
    button.button(buttonPreview, 'Generate password', lambda: updatePassword.updatePassword(entryPassword, array), 1)
    button.button(buttonPreview, 'Save password', lambda: saveFrame.saveFrame(entryPassword), 2)