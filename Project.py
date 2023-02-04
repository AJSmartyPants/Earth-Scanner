from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import webview
import webbrowser
from tkinter import messagebox as mb
import json
from subprocess import Popen
import subprocess
import os

#creating the window
root = Tk()
root.configure(bg = '#CCCCFE')
root.title("Earth Scanner")
#root.state('zoomed')
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#creating the functions
def hello():
    print('hello')
def scananimal():
    #webview.create_window('Scan_Animal', 'index.html')#, width = 800, height = 600)
    subprocess.call(["python", "Earth-Scanner/CameraAnimal.py"])
    #webbrowser.open_new_tab(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\index.html')
def scanplant():
    subprocess.call(["python", "Earth-Scanner/CameraPlant.py"])
def quizfunc():
    #Popen(['python',r"C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Quizcode.py"])
    #exec(open('Earth-Scanner/Quizcode.py').read())
    subprocess.call(["python", "Earth-Scanner/Quizcode.py"])
def knowfunc():
    subprocess.call(["python", "Earth-Scanner/KnowledgeHub.py"])
def arfunc():
    subprocess.call(["python", "Earth-Scanner/AR.py"])

#making all the variables
winwidth = root.winfo_vrootwidth()
winheight = root.winfo_vrootheight()
print(winwidth, winheight)
saimg = Image.open(r"C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\ScanAnimalIcon.png").resize((100, 100), Image.LANCZOS)
saimgf = ImageTk.PhotoImage(saimg)
spimg = Image.open(r"C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\ScanPlantIcon.png").resize((100, 100), Image.LANCZOS)
spimgf = ImageTk.PhotoImage(spimg)
infimg = Image.open(r"C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\KnowHubIcon.png").resize((100, 100), Image.LANCZOS)
infimgf = ImageTk.PhotoImage(infimg)
qimg = Image.open(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\QuizIcon.png').resize((100, 100), Image.LANCZOS)
qimgf = ImageTk.PhotoImage(qimg)
arimg = Image.open(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\ARIcon.png').resize((100, 100), Image.LANCZOS)
arimgf = ImageTk.PhotoImage(arimg)

sabn = Button(root, text = 'Scan Animals', font = ('Britannic Bold', 20, 'bold'), fg = '#0018b8', activeforeground = '#0022ff', bg = '#82e2ff', activebackground = '#b5eeff', image = saimgf, compound = BOTTOM, command = scananimal)#, width = int(winwidth/10), height = int(winheight/10))
spbn = Button(root, text = 'Scan Plants', font = ('Britannic Bold', 20, 'bold'), fg = '#0018b8', activeforeground = '#0022ff', bg = '#82e2ff', activebackground = '#b5eeff', image = spimgf, compound = BOTTOM, command = scanplant)#, width = int(winwidth/10), height = int(winheight/10))
ibn = Button(root, text = 'Knowledge Hub', font = ('Britannic Bold', 20, 'bold'), fg = '#0018b8', activeforeground = '#0022ff', bg = '#82e2ff', activebackground = '#b5eeff', image = infimgf, compound = BOTTOM, command = knowfunc)#, width = int(winwidth/10), height = int(winheight/10))
qbn = Button(root, text = 'Quiz Game', font = ('Britannic Bold', 20, 'bold'), fg = '#0018b8', activeforeground = '#0022ff', bg = '#82e2ff', activebackground = '#b5eeff', image = qimgf, compound = BOTTOM, command = quizfunc)#, width = int(winwidth/10), height = int(winheight/10))
arbn = Button(root, text = 'Augmented Reality', font = ('Britannic Bold', 20, 'bold'), fg = '#0018b8', activeforeground = '#0022ff', bg = '#82e2ff', activebackground = '#b5eeff', image = arimgf, compound = BOTTOM, command = arfunc)#, width = int(winwidth/10), height = int(winheight/10))
#hsb = Button(root, text = 'Scan', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
#             activebackground = '#99FFFF', height = 250, image = scanicon, compound = BOTTOM, command = scanscr)

#sabn.pack(side=LEFT, anchor=NW, fill=X, expand=True, padx=int(winwidth/100))
#spbn.pack(side=LEFT, anchor=NW, fill=X, expand=True, padx=int(winwidth/100))
#arbn.pack(side=LEFT, anchor=NW, fill=X, expand=True, padx=int(winwidth/100))
#ibn.pack(side=LEFT, anchor=NW, fill=X, expand=True, padx=int(winwidth/100))
#qbn.pack(side=LEFT, anchor = NW, fill=X, expand=True, padx = int(winwidth/100))

pad = 5
sabn.grid(row = 0, column = 0, sticky = "news", padx=pad, pady=pad)
spbn.grid(row = 0, column = 1, sticky = "news", padx=pad, pady=pad)
arbn.grid(row = 1, column = 0, sticky = "news", columnspan=2, padx=pad, pady=pad)
ibn.grid(row = 2, column = 0, sticky = "news", padx=pad, pady=pad)
qbn.grid(row = 2, column = 1, sticky = "news", padx=pad, pady=pad)

mainloop()
