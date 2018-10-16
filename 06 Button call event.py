from tkinter import *
root = Tk()

def printName(event):
	print("Hello my name is bucky")

button_1 = Button(root, text="Hello")
button_1.bind("<Button-1>",printName)
button_1.pack()



root.mainloop()