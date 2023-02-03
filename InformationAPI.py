import requests
import pandas as pd
import json
import tkinter as tk
from tkinter import ttk
#import urllib2
from bs4 import BeautifulSoup
#from sketch import label

#r = requests.get('https://index.html')
with open(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\index.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
#soup = BeautifulSoup(open(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\index.html')).read()
#soup2 = BeautifulSoup(soup.content, 'html5lib')
labeltext = soup.select_one('p').text
print(labeltext)

# Load the data from the file
#with open(r"Earth-Scanner\results.json", "r") as file:
#    data = json.load(file)

# Use the data as needed
#results = data

def display_information(animalname):
    name = animalname
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'wCrBnEMU6ayQP7U+43e7/A==wd7RvCoQVu5k3C2x'})
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        for item in data:
            text_widget.insert('end', "Name: " + item["name"] + "\n")
            text_widget.insert('end', "Taxonomy:\n")
            taxonomy = item["taxonomy"]
            for key in taxonomy:
                text_widget.insert('end', "  " + key.capitalize() + ": " + taxonomy[key] + "\n")
            text_widget.insert('end', "Locations:\n")
            locations = item["locations"]
            text_widget.insert('end', str(locations) + "\n")
            text_widget.insert('end', "Characteristics:\n")
            characteristics = item["characteristics"]
            for key in characteristics:
                text_widget.insert('end', "  " + key.capitalize() + ": " + characteristics[key] + "\n")
    else:
        text_widget.insert('end', "Error: " + str(response.status_code) + " " + response.text + "\n")

root = tk.Tk()
root.title("Information")

text_widget = tk.Text(root, height=20, width=50)
text_widget.pack()

display_button = ttk.Button(root, text="Display Information", command=lambda:display_information(labeltext))
display_button.pack()

root.mainloop()