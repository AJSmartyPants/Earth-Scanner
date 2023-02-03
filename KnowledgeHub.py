#Importing Module
from tkinter import *

#Creating Object
root = Tk()

#Creating Window Size
root.geometry( '1000x700' )
root.configure(background = '#CCCCFE')
root.state('zoomed')

#Text Label
def show():
    #label.config( text = clicked.get() )

    label.bind('<Configure>', lambda e: label.config(wraplength=root.winfo_width()))
    if clicked.get() == 'Caring for Plants':
        label.config(state = NORMAL)
        label.delete(1.0, END)
        label.insert('end', "Here's how to care for your plants!")#, yscrollcommand=v.set)
        label.config(state = DISABLED)
    elif clicked.get() == 'Animals and Safety':
        label.config(state = NORMAL)
        label.delete(1.0, END)
        label.insert('end', "How do you stay safe around animals? How do you make sure the animals around you are safe? What should and shouldn't you do to keep an animal safe?")#, yscrollcommand=v.set)
        label.config(state = DISABLED)
    elif clicked.get() == 'Plants to Watch Out For':
        label.config(state = NORMAL)
        label.delete(1.0, END)
        label.insert('end',"Here are some common (and uncommon!) toxic plants to watch out for.")#, yscrollcommand=v.set)
        label.config(state = DISABLED)
    elif clicked.get() == 'Animals and Insects to Watch Out For':
        label.config(state = NORMAL)
        label.delete(1.0, END)
        label.insert('end', "Stay away from these animals and insects, and learn how to spot them!")#, yscrollcommand=v.set)
        label.config(state = DISABLED)
    else:
        label.config(state = NORMAL)
        label.delete(1.0, END)
        label.insert('end', "Please choose what you would like to learn about today.")#, yscrollcommand=v.set)
        label.config(state = DISABLED)
    
#Dropdown menu options
options = [
    'Caring for Plants',
    'Animals and Safety', 
    'Plants to Watch Out For', 
    'Animals and Insects to Watch Out For'
]

#Datatype of menu text
clicked = StringVar()

#Menu text
clicked.set('What do you want to learn about today?')

#Title Label
title = Label( root , text = "Knowledge Hub", font = ('Britannic Bold', 45, 'normal'), background = '#CCCCFE', foreground= '#00123b')

#Create Dropdown options
dropdown = OptionMenu( root , clicked , *options )
dropdown.config(font = ("Britannic Bold", 20, 'normal'), foreground = '#0044e3', activeforeground = '#002c91')

#Create Button
button = Button( root , text = 'View information' , font = ("Britannic Bold", 20, 'normal'), command = show )

#Labeling
v=Scrollbar(root, orient='vertical')
v.pack(side=RIGHT, fill='y')
label = Text( root, font = ("Britannic Bold", 20, 'normal'), background = '#CCCCFE', foreground= '#0044e3', wrap = WORD, yscrollcommand = v.set)
label.insert('end', "Please choose what you would like to learn about today.")
#label.delete(1.0, END)
label.config(state = DISABLED)
v.config(command=label.yview)

title.pack()
dropdown.pack()
button.pack()
label.pack()

#Fonting and sizing the options in the Menu


#Execute Tkinter
mainloop()