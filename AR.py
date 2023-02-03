from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()

#Creating Window Size
root.geometry( '1000x700' )
root.configure(background = '#CCCCFE')
root.state('zoomed')

global qrsaimgf
qrsaimg = Image.open(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\Sea Animals.png').resize((200, 200), Image.LANCZOS)
qrsaimgf = ImageTk.PhotoImage(qrsaimg)
global qrlaimgf
qrlaimg = Image.open(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\Sea Animals.png').resize((200, 200), Image.LANCZOS)
qrlaimgf = ImageTk.PhotoImage(qrlaimg)
global qrbimgf
qrbimg = Image.open(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\Sea Animals.png').resize((200, 200), Image.LANCZOS)
qrbimgf = ImageTk.PhotoImage(qrbimg)
global qriimgf
qriimg = Image.open(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\Sea Animals.png').resize((200, 200), Image.LANCZOS)
qriimgf = ImageTk.PhotoImage(qriimg)
global qrpimgf
qrpimg = Image.open(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\Sea Animals.png').resize((200, 200), Image.LANCZOS)
qrpimgf = ImageTk.PhotoImage(qrpimg)
global qrfimgf
qrfimg = Image.open(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\Images\Sea Animals.png').resize((200, 200), Image.LANCZOS)
qrfimgf = ImageTk.PhotoImage(qrfimg)
#Text Label
def show():
    #label.config( text = clicked.get() )
    if clicked.get() == 'Sea Animals':
        global qrsaimgf
        qrcode.config(image = qrsaimgf)
        root.update_idletasks()
    elif clicked.get() == 'Land Animals':
        global qrlaimgf
        qrcode.config(image = qrlaimgf)
    elif clicked.get() == 'Birds':
        global qrbimgf
        qrcode.config(image = qrbimgf)
    elif clicked.get() == 'Insects':
        global qriimgf
        qrcode.config(image = qriimgf)
    elif clicked.get() == 'Plants':
        global qrpimgf
        qrcode.config(image = qrpimgf)
    elif clicked.get() == 'Flowers':
        global qrfimgf
        qrcode.config(image = qrfimgf)
#Dropdown menu options
options = [
    'Sea Animals',
    'Land Animals', 
    'Birds', 
    'Insects',
    'Plants',
    'Flowers'
]

#Datatype of menu text
clicked = StringVar()

#Menu text
clicked.set('Choose the AR objects you want to explore!')

#Title Label
title = Label(root , text = "Augmented Reality", font = ('Britannic Bold', 45, 'normal'), background = '#CCCCFE', foreground= '#00123b')

#Create Dropdown options
dropdown = OptionMenu( root , clicked , *options )
dropdown.config(font = ("Britannic Bold", 20, 'normal'), foreground = '#0044e3', activeforeground = '#002c91')

#Create Button
button = Button( root , text = 'Click to refresh QR code' , font = ("Britannic Bold", 20, 'normal'), command = show )

#Labeling
#v=Scrollbar(root, orient='vertical')
#v.pack(side=RIGHT, fill='y')
qrcode = Label(root, background = '#CCCCFE')#, font = ("Britannic Bold", 20, 'normal'), background = '#CCCCFE', foreground= '#0044e3')
#label.insert('end', "Please choose what you would like to learn about today.")
#label.delete(1.0, END)

title.pack()
dropdown.pack()
button.pack()
qrcode.pack()

show()
mainloop()