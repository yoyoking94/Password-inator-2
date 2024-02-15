from tkinter import *

def checked(labels, variable, x, array):
    if variable == 1:
        array.append(labels[x])
    else:
        for arr in array:
            if arr == labels[x]:
                array.remove(labels[x])