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
#import Quizcode

#creating the window with a menubar, and adding menubar functions
root = Tk()
root.configure(bg = '#CCCCFE')
root.state('zoomed')
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#creating the functions
def hello():
    print('hello')
def scananimal():
    #webview.create_window('Scan_Animal', 'index.html')#, width = 800, height = 600)
    webbrowser.open_new_tab(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\index.html')
def quizfunc():
    #Popen(['python',r"C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Quizcode.py"])
    #exec(open('Earth-Scanner/Quizcode.py').read())
    subprocess.call(["python", "Earth-Scanner/Quizcode.py"])
def knowfunc():
    subprocess.call(["python", "Earth-Scanner/KnowledgeHub.py"])

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

sabn = Button(root, text = 'Scan Animals', font = ('Britannic Bold', 20, 'bold'), fg = '#0018b8', activeforeground = '#0022ff', bg = '#82e2ff', activebackground = '#b5eeff', image = saimgf, compound = BOTTOM, command = scananimal)#, width = int(winwidth/10), height = int(winheight/10))
spbn = Button(root, text = 'Scan Plants', font = ('Britannic Bold', 20, 'bold'), fg = '#0018b8', activeforeground = '#0022ff', bg = '#82e2ff', activebackground = '#b5eeff', image = spimgf, compound = BOTTOM)#, width = int(winwidth/10), height = int(winheight/10))
ibn = Button(root, text = 'Knowledge Hub', font = ('Britannic Bold', 20, 'bold'), fg = '#0018b8', activeforeground = '#0022ff', bg = '#82e2ff', activebackground = '#b5eeff', image = infimgf, compound = BOTTOM, command = knowfunc)#, width = int(winwidth/10), height = int(winheight/10))
qbn = Button(root, text = 'Quiz Game', font = ('Britannic Bold', 20, 'bold'), fg = '#0018b8', activeforeground = '#0022ff', bg = '#82e2ff', activebackground = '#b5eeff', image = qimgf, compound = BOTTOM, command = quizfunc)#, width = int(winwidth/10), height = int(winheight/10))
#hsb = Button(root, text = 'Scan', font=('Britannic Bold', 20, 'bold'), fg = '#7700CC', activeforeground = '#0099FF', bg = '#9999FF',
#             activebackground = '#99FFFF', height = 250, image = scanicon, compound = BOTTOM, command = scanscr)

sabn.pack(side=LEFT, anchor=NW, padx=int(winwidth/100))
spbn.pack(side=LEFT, anchor=NW, padx=int(winwidth/100))
ibn.pack(side=LEFT, anchor=NW, padx=int(winwidth/100))
qbn.pack(side=LEFT, anchor = NW, padx = int(winwidth/100))
mainloop()
