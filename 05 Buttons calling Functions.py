from tkinter import *
root = Tk()

def printName():
	print("Hello my name is bucky")

button_1 = Button(root, text="Hello", command=printName)

button_1.pack()



root.mainloop()