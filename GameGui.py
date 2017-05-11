__author__ = 'Lina Andersson'

from tkinter import*
from PIL import ImageTk, Image
import os

class GUI():
    #create window
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.root.geometry("400x600+30+30")
        self.root.configure(bg="#4fc8fc")
        self.imageReferences = []

    def setIcon(self, icon):
        self.root.iconbitmap(os.path.abspath(icon))

    def setTitel(self, title):
        self.root.title(title)

        #Read in images and save references in list
    def readImage(self, path):
        nameImage = path
        self.img = Image.open(nameImage)
        self.buttonImg = ImageTk.PhotoImage(self.img)

        self.imageReferences.append(self.buttonImg)
        return self.buttonImg

    #Function for creation of text objects
    def text(self, root, text, xPos, yPos, size, backgroundColor, textColor, textWidth, textHeight,  event = lambda X: None):
        self.textLabel = Label(root, text= text, font = ("Helvetica", size), fg = textColor, bg= backgroundColor, justify = LEFT, wraplength = 300)
        self.textLabel.bind("<Button-1>", event)
        self.textLabel.place(x = xPos, y = yPos, width = textWidth, height = textHeight)
        return self.textLabel

    def destroy(self):
        self.textLabel.destroy()

    #Used to create buttons
class GameButton():
    def __init__(self, name, gui):
        self.name = name
        self.buttonImg = gui.readImage(self.name + ".png")

    #Create the button and gives it a position, look and the event that should happened when it is pressed
    def createLabel(self, root, xSize, ySize, xPos, yPos, event = lambda X: None):
        self.buttonLabel = Label(root, image = self.buttonImg, height = ySize, width= xSize, borderwidth = 0)
        self.buttonLabel.bind("<Button-1>", event)

        #Set position of object
        self.buttonLabel.place(x = xPos, y = yPos)
        self.xPosition = xPos
        self.yPosition = yPos

    def getXPosition(self):
        return self.xPos

    def getYPosition(self):
        return self.yPos

    def setPosition(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.buttonLabel.place(x = self.xPos, y = self.yPos)

    def destroy(self):
        self.buttonLabel.destroy()