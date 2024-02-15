import os
from tkinter import *

def padlockImg(displayFrame, path):
    width = 600
    height = 150
    global image
    image = PhotoImage(file = path).zoom(1).subsample(5)
    canvas = Canvas(displayFrame, width=width, height=height, bd=0, highlightthickness=0, bg='#f6a522')
    canvas.create_image(width/2, height/2, image=image)
    canvas.pack(pady=25, fill=X)