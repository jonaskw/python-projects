from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
import os
from os import listdir
from os.path import isfile, join
import pathlib

root = Tk()
root.title('Image Viewer')

mypath = pathlib.Path().resolve()

files_in_folder = [f for f in listdir(mypath) if isfile(join(mypath, f))]

image_names = []
for i in files_in_folder:
    if "png" in i or "jpg" in i:
        if i != "back.png" and i != "forward.png" and i != "exit.png":
            image_names.append(i)

image_list = []
for i in range(len(image_names)):
    image_list.append(ImageTk.PhotoImage(Image.open(image_names[i])))

status = Label(root, text = "Image 1 of " + str(len(image_names)), font = font.Font(size = 12))

mylabel = Label(image = image_list[0])
mylabel.grid(row = 0, column = 0, columnspan = 3)
title = Label(root, text = image_names[0], font = font.Font(size = 12, weight = "bold"))

def forward(img_num):
    global mylabel, button_forward, button_back, image_list, title, status
    
    mylabel.grid_forget()
    mylabel['image'] = image_list[img_num+1]
    button_forward['command'] = lambda: forward (img_num+1)
    button_back['command'] = lambda: back (img_num-1)
    button_back['state'] = NORMAL
    status['text'] = "Image " + str(img_num + 2) + " of " + str(len(image_names))
    title['text'] = image_names[img_num+1]
    
    if img_num >= len(image_names) - 2:
        button_forward['state'] = DISABLED
    else:
        button_forward['state'] = NORMAL
    
    inserting()

def back(img_num):
    global mylabel, button_forward, button_back, image_list, title, status
    
    mylabel['image'] = image_list[img_num+1]
    button_forward['command'] = lambda: forward (img_num+1)
    button_back['command'] = lambda: back (img_num-1)
    button_forward['state'] = NORMAL
    status['text'] = "Image " + str(img_num + 2) + " of " + str(len(image_names))
    title['text'] = image_names[img_num-3]
    
    if img_num <= len(image_names) - 5:
        button_back['state'] = DISABLED
    else:
        button_back['state'] = NORMAL
        
    inserting()

image_back = ImageTk.PhotoImage(Image.open("back.png").resize((35, 35)))
image_forward = ImageTk.PhotoImage(Image.open("forward.png").resize((35, 35)))
image_exit = ImageTk.PhotoImage(Image.open("exit.png").resize((35, 35)))

button_back = Button(root, text = "<<", image = image_back, command = lambda: back(0), state = DISABLED, borderwidth = 0)
button_exit = Button(root, text = "Exit", command=root.destroy, image = image_exit, borderwidth = 0)
button_forward = Button(root, text = ">>", image = image_forward,borderwidth = 0, command = lambda: forward(0))

def inserting():
    button_back.grid(row = 2, column = 0)
    button_exit.grid(row = 2, column = 1)
    button_forward.grid(row = 2, column = 2)
    status.grid(row = 3, column = 0, columnspan = 3)
    title.grid(row = 0, column = 0, columnspan = 3)
    mylabel.grid(row = 1, column = 0, columnspan = 3)

inserting()

root.mainloop()
