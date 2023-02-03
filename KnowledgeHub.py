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
        label.insert('end', "Here's how to care for your plants! Keep the soil moist. Either the soil is too dry or overwatered, it can be an obstruction in the growth of the plant. In some cases, less or overwatering the plant also destroys it. Plants which have lush, thick leaves need more water than plants with waxy or leathery leaves. If you see mould formations on the surface of the soil or the water is standing at the bottom of the container that means the plant has been overwatered. Give water when the soil of plant turns lighter in colour or seems cracked. Standing water can kill plants. If you see standing water in or under the pot, then pour it out.")#, yscrollcommand=v.set)
        label.config(state = DISABLED)
    elif clicked.get() == 'Animals and Safety':
        label.config(state = NORMAL)
        label.delete(1.0, END)
        label.insert('end', "How do you stay safe around animals? How do you make sure the animals around you are safe? What should and shouldn't you do to keep an animal safe?")#, yscrollcommand=v.set)
        label.config(state = DISABLED)
    elif clicked.get() == 'Plants to Watch Out For':
        label.config(state = NORMAL)
        label.delete(1.0, END)
        label.insert('end',"Here are some common (and uncommon!) toxic plants to watch out for. Poison Ivy is a hairy, ropelike vine with three shiny green leaves budding from one small stem or a low shrub without a climbing vine that may have yellow or green flowers and white to green-yellow or amber berries. Poison Oak is a shrub with three leaves that may have yellow or green flowers and clusters of green-yellow or white berries. Poison Sumac is a woody shrub with stems having 7-13 leaves arranged in pairs and may have glossy, pale yellow, or cream-colored berries.")#, yscrollcommand=v.set)
        label.config(state = DISABLED)
    elif clicked.get() == 'Animals and Insects to Watch Out For':
        label.config(state = NORMAL)
        label.delete(1.0, END)
        label.insert('end', "Stay away from these animals and insects, and learn how to spot them! The Cow Killer, also known as the Velvet Wasp, can be found in the southern part of Maryland. It is not lethal to humans unless stepped on in large numbers, in which case the victim may experience a double dose of venom from stinging and biting. Children and people with suppressed immune systems are more at risk. The Red Imported Fire Ant is aggressive and one of the top 10 threats to agriculture. The USDA has not been successful in killing them, and they can chase and sting individuals. They have been known to cause fatalities, especially in young people, and cannot be guaranteed to be eliminated by pest control. Blister Beetles produce a compound called cantharidin, which was once believed to be an aphrodisiac but can cause severe dermatitis and death if ingested. The Japanese Oriental Wasp is one of the most aggressive insects and can deliver a high amount of venom, causing excruciating pain. The wasp is found in remote locations and has a high death rate. The Black Widow is not an insect but a spider. Its bite is not fatal but can cause weeks or months of misery. Some people may experience lasting effects from the bite.")#")#, yscrollcommand=v.set)
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