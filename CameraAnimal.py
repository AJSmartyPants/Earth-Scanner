from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import webbrowser
import http.server
import socketserver
import os
#import ml5 as ml5555
#img = ''
#modelURL = "https://teachablemachine.withgoogle.com/models/JCF26yjL3/"
#PORT = 8080
#handler = http.server.SimpleHTTPRequestHandler
#os.chdir(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\index.html')

#classifier = ml5.imageClassifier(modelURL + 'model.json')
def scan():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        # Display the frame
        cv2.imshow("Camera", frame)
        #Check if the user pressed 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord(' '):
            cv2.imwrite(r"C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\object.jpg", frame)
            break
    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    #with socketserver.TCPServer(("localhost", PORT), handler) as httpd:
    #    print("Serving on port", PORT)
    #    httpd.serve_forever()
    #webbrowser.open_new_tab(r'C:\Users\tinao\OneDrive\Desktop\Scanning Scouts Project\Earth-Scanner\index.html')
    webbrowser.open_new_tab("http://127.0.0.1:5500/Earth-Scanner/index.html")
    #cv2.imshow("Picture Taken", frame)
    # Define the image variable that we will use to extract medicine info from
    #global img
    #img = frame
    #grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #contrast_gray = cv2.convertScaleAbs(grayimg, alpha=1.5, beta=0)
    #cv2.imshow('Grayscale', contrast_gray)
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #classifyVideo()
    #print(text)
scan()
#def classifyVideo():
#    global img
#    classifier.classify(img, gotResult)
#def gotResult(error, results):
#    if (error):
#        print(error)
#        return
#    #print(results[0])
#   print(results[0].label)
#   classifyVideo()