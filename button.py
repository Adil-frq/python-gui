from tkinter import *
root = Tk()
def button_clicked():
    myLabel1 = Label(root, text=" button clicked")
    myLabel1.grid(row=2,column=1)
    


Button(root, text="click me!").grid(row=0,column=1)
Button(root, text="Disabled button!", state=DISABLED).grid(row=1,column=0)
Button(root, text="Wider button!", padx=50).grid(row=1,column=1)
Button(root, text="Wider button!", padx=50, pady=50).grid(row=1,column=2)
Button(root, text="Click me for function call!", command=button_clicked).grid(row=1,column=3)
Button(root, text="colour button", fg="white", bg="black").grid(row=2,column=2)
Button(root, text="colour button", fg="white", bg="#000000").grid(row=2,column=2)
root.mainloop()

#either you have to use grid or pack at the same time you can't use both