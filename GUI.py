#!/usr/bin/env python
# coding: utf-8

# In[4]:

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as font
import os

root = tk.Tk()
root.title("Major Project")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background="black")

welcome=Label(root,text="PIANO TUNE GENERATOR",font=("comic sans ms",'30',"bold"),fg="white",bd=10,anchor=W,bg="black")
welcome.place(x=250)
welcome.pack()

#c = tk.Canvas(root, width = 600, height = 330,bg="black")
#c.pack()


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open('piano.jpg')
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.entry1 = Entry(self)
        self.entry1.pack(fill=BOTH)

        myFont = font.Font(size=13)

	#label of entry
        labelAbove = Label(self, text="Enter name of the model",font=("courier new",'17',"bold"),fg="black",bd=10,anchor=W,bg="SlateGray3")
        labelAbove.place(x=470,y=200)

	#entry button
        entryButton = Entry(self)
        entryButton.place(x=525,y=260, height=30, width=220)
        def genmusic ():
            name=entryButton.get()
            os.system("python3 predict.py "+name)

	# creating a button instance
        outputButton = Button(self, text="Generate the MIDI file",activeforeground="black",fg="blue",command=genmusic)
        # placing the button on my window
        outputButton.place(x=640,y=320,height=30, width=300,anchor=CENTER)
        outputButton['font'] = myFont


	# creating a button instance
        quitButton = Button(self, text="Quit!", activeforeground="black", fg="red",command = root.destroy)
      	# placing the button on my window
        quitButton.place(x=600,y=350, height=30, width=70)
        quitButton['font'] = myFont
        #quitButton.pack()





    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



e = Example(root)
e.pack(fill=BOTH, expand=YES)


root.mainloop()
