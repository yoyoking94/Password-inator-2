from tkinter import *

## ==== Import backend ==== ##
from Backend import checked

def checkbox(checkboxPreview, labels, variables, x, array):
        variable = variables[x]
        checkbox = Checkbutton(checkboxPreview, text=labels[x], variable=variable, command=lambda : checked.checked(labels, variable.get(), x, array), font=('Helvetica', 15), bg='#f6a522',fg='#000')
        checkbox.grid(row=x+1, column=1, sticky="w") 
        return checkbox