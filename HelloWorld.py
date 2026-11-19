#tkinker is used to create GUI application
#in tkinter evary thing is a wigit (text , button and so on)
#first you have to create window that we named root

from tkinter import *
root = Tk() # this is windows
#Creating a lable
myLabel = Label(root, text="Hello World!")
#showing it onto screen
myLabel.pack()
# program runs an ends if you want to run continuesly then we have to make loop

root.mainloop()

